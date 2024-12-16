from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class Booking(models.Model):
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
    # Ensure date is not None
    if self.date is None:
        raise ValidationError('Date cannot be empty.')

    # Ensure bookings are not made on Sundays
    if self.date.weekday() == 6:  # 6 corresponds to Sunday
        raise ValidationError('Bookings cannot be made on Sundays.')


class DisabledTimeSlot(models.Model):
    date = models.DateField()
    time_slot = models.TimeField(choices=Booking.TIMESLOTS)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ['date', 'time_slot']
