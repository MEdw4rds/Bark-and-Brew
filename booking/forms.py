from django import forms
from .models import Booking, DisabledTimeSlot


class BookingForm(forms.ModelForm):
    """
    Creates form to be displayed in :view:`booking.book_time_slot` applying a
    widget to the date field and using the date and timeslot fields.
    """
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['date', 'time_slot']


class EditBookingForm(forms.ModelForm):
    """
    Creates form to be displayed in :view:`booking.edit_booking` applying a
    widget to the date field and using the date and timeslot fields.
    """
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['date', 'time_slot']


class DisabledTimeSlotForm(forms.ModelForm):
    """
    Creates form to be displayed only in the admin panel to disable certain
    timeslots for the superuser.
    """
    class Meta:
        model = DisabledTimeSlot
        fields = ['date', 'time_slot', 'reason']
