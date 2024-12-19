from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Booking, DisabledTimeSlot
from .forms import BookingForm, EditBookingForm


def profile(request):
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
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
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
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        if 'cancel' in request.POST:
            booking.is_canceled = True
            booking.save()
            return redirect('profile')
        elif 'delete' in request.POST:
            booking.delete()
            return redirect('profile')
        else:
            form = EditBookingForm(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                return redirect('profile')
    else:
        form = EditBookingForm(instance=booking)
    return render(request, 'booking/edit_booking.html', {
        'form': form,
        'booking': booking
    })


@login_required
def booking_success(request):
    return render(request, 'booking/booking_success.html')
