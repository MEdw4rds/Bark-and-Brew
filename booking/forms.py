from django import forms
from .models import Booking, DisabledTimeSlot


class BookingForm(forms.ModelForm):
    date = forms.DateField( 
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['date', 'time_slot']

    def clean_date(self):
        date = self.cleaned_data['date']
        if date.weekday() == 6:  # Sunday
            raise forms.ValidationError("Bookings cannot be made on Sundays.")
        return date


class DisabledTimeSlotForm(forms.ModelForm):
    class Meta:
        model = DisabledTimeSlot
        fields = ['date', 'time_slot', 'reason']
