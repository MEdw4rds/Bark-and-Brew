from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import Booking, DisabledTimeSlot
from .forms import BookingForm, EditBookingForm


def profile(request):
    """
    Display a list of Active and cancelled bookings by the current user.
    :model:`booking.Booking`
    **Context**

    ``booking_id``
        The Id of a :model:`booking.Booking`.
    ``booking``
        The instance of the Booking retrieved by the booking_id
        :model:`booking.Booking`
    ``active_bookings``
        An instance to check if the current Booking is active
        :form:`booking.Booking`.
    ``cancelled_bookings``
        An instance to check if the current Booking is cancelled.
        :form:`booking.Booking`.

    **Template:**

    :template:`booking/profile.html`
    """
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        if booking_id:
            booking = get_object_or_404(
                Booking,
                id=booking_id,
                user=request.user
                )
            if booking.is_canceled:
                booking.delete()
                return redirect('profile')

    active_bookings = Booking.objects.filter(
        user=request.user, is_canceled=False
        )
    cancelled_bookings = Booking.objects.filter(
        user=request.user, is_canceled=True
        )
    return render(request, 'booking/profile.html', {
        'active_bookings': active_bookings,
        'cancelled_bookings': cancelled_bookings
    })


@login_required
def book_time_slot(request):
    """
    Display a list of Active and cancelled bookings by the current user.
    :model:`booking.Booking`
    **Context**

    ``form``
        The booking form in :form:`booking.BookingForm`.
    ``booking``
        The instance of the BookingForm sent by user.
        :form:`booking.BookingForm`
    ``selected_date``
        The date taken from a GET request if it is true the date
        is converted into datetime.
    ``taken_time_slots``
        An instance to check if the current Booking taken or has been
        disabled by the administrator.
        :model:`booking.Booking`.

    **Template:**

    :template:`booking/book_time_slot.html`
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            try:
                booking.save()
                return redirect('booking_success')
            except ValidationError as e:
                messages.add_message(request, messages.ERROR, e.message)
        else:
            for error in form.errors.values():
                messages.add_message(request, messages.ERROR, error)
    else:  # This is for the GET request
        form = BookingForm()

    selected_date = request.GET.get('date', None)
    if selected_date:
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        queryset = Booking.objects.filter(
            date=selected_date, is_canceled=False
            )
        taken_time_slots = queryset.values_list('time_slot', flat=True)
        querysetTwo = DisabledTimeSlot.objects.filter(
            date=selected_date
            )
        disabled_time_slots = querysetTwo.values_list('time_slot', flat=True)
    else:
        taken_time_slots = []
        disabled_time_slots = []

    return render(request, 'booking/book_time_slot.html', {
        'form': form,
        'taken_time_slots': taken_time_slots,
        'disabled_time_slots': disabled_time_slots
    })


@login_required
def edit_booking(request, booking_id):
    """
    Display one booking for edit.

    **Context**
    ``booking``
        An instance of :model:`booking.Booking`.
    ``form``
    An instance of :form:`booking.EditBookingForm`.

    **Template**

    :template:`booking/edit_booking.html`
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        if 'cancel' in request.POST:
            booking.is_canceled = True
            try:
                booking.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Booking cancelled successfully.')
                return redirect('profile')
            except ValidationError as e:
                messages.add_message(request, messages.ERROR, e.message)
        elif 'delete' in request.POST:
            booking.delete()
            messages.add_message(request, messages.SUCCESS,
                                 'Booking deleted successfully.')
            return redirect('profile')
        else:
            form = EditBookingForm(request.POST, instance=booking)
            if form.is_valid():
                try:
                    form.save()
                    messages.add_message(request, messages.SUCCESS,
                                         'Booking updated successfully.')
                    return redirect('profile')
                except ValidationError as e:
                    messages.add_message(request, messages.ERROR, e.message)
            else:
                for error in form.errors.values():
                    messages.add_message(request, messages.ERROR, error)
    else:
        form = EditBookingForm(instance=booking)

    return render(request, 'booking/edit_booking.html', {
            'form': form,
            'booking': booking
        })


@login_required
def booking_success(request):
    return render(request, 'booking/booking_success.html')
