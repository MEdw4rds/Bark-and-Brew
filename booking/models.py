from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class Booking(models.Model):
    """
    Stores a single booking entry related to :model:`auth.User`.
    """
    TIMESLOTS = [
        (datetime.time(hour=8), '08:00'),
        (datetime.time(hour=10), '10:00'),
        (datetime.time(hour=12), '12:00'),
        (datetime.time(hour=14), '14:00'),
        (datetime.time(hour=16), '16:00'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField(choices=TIMESLOTS)
    is_canceled = models.BooleanField(default=False)

    class Meta:
        unique_together = ['date', 'time_slot']

    def clean(self):
        super().clean()
        if self.date < datetime.date.today():
            raise ValidationError('You cannot book a past date.')
        if self.date.weekday() == 6:  # 6 corresponds to Sunday
            raise ValidationError('Bookings cannot be made on Sundays.')
        disabled_time_slots = DisabledTimeSlot.objects.filter(
            date=self.date, time_slot=self.time_slot)
        if disabled_time_slots.exists():
            raise ValidationError('The selected time slot is disabled.')


class DisabledTimeSlot(models.Model):
    """
    Stores a single disabled timeslot entry only
    availible through the admin panel.
    """
    date = models.DateField()
    time_slot = models.TimeField(choices=Booking.TIMESLOTS)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ['date', 'time_slot']
