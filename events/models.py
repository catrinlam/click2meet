from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=255)
    description = models.TextField()
    organizer = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return self.name

    @property
    def total_tickets_sold(self):
        return sum(booking.quantity for ticket in self.ticket_types.all() for booking in ticket.bookings.all())


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/%Y/%m/%d/')

    def __str__(self):
        return f"Image for {self.event.name}"
    

class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_types')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    @property
    def remaining_quantity(self):
        return self.quantity - sum(self.bookings.values_list('quantity', flat=True))

    def __str__(self):
        return f"{self.name} ({self.event})"