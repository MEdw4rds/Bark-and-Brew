from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking, DisabledTimeSlot
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def book_time_slot(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = BookingForm()

    selected_date = request.GET.get('date', None)
    if selected_date:
        selected_date = datetime.datetime.strptime(selected_date, '%Y-%m-%d').date()
        taken_time_slots = Booking.objects.filter(date=selected_date, is_canceled=False).values_list('time_slot', flat=True)
        disabled_time_slots = DisabledTimeSlot.objects.filter(date=selected_date).values_list('time_slot', flat=True)
    else:
        taken_time_slots = []
        disabled_time_slots = []

    return render(request, 'booking/book_time_slot.html', {
        'form': form,
        'taken_time_slots': taken_time_slots,
        'disabled_time_slots': disabled_time_slots
    })
