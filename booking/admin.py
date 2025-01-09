from django.contrib import admin
from .models import Booking, DisabledTimeSlot

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Displays list of current bookings in the admin panel.
    allows searching by user and date.
    """

    list_display = ('user', 'date', 'is_canceled')


@admin.register(DisabledTimeSlot)
class DisabledTimeSlotAdmin(admin.ModelAdmin):
    """
    Displays list of current timeslots disabled by the admin in the admin
    panel. Allows searching by Date, timeslot and Reason.
    """

    list_display = ('date', 'time_slot', 'reason')
