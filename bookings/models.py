from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from events.models import TicketType


class Booking(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name='bookings')
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    booked_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )

    class Meta:
        ordering = ['-booked_at']

    def __str__(self):
        return f"{self.user.username} - {self.ticket_type} x {self.quantity}"

    @property
    def total_price(self):
        return self.ticket_type.price * self.quantity
