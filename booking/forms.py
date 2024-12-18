from django import forms
from .models import Booking, DisabledTimeSlot


class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['date', 'time_slot']


class EditBookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['date', 'time_slot']


class DisabledTimeSlotForm(forms.ModelForm):
    class Meta:
        model = DisabledTimeSlot
        fields = ['date', 'time_slot', 'reason']
