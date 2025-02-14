from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'ticket_type', 'quantity', 'booked_at', 'payment_status'
    )
    search_fields = ('user__username', 'ticket_type__name')
    list_filter = ('payment_status', 'booked_at')
