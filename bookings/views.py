from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from events.models import Event, TicketType
from django.db.models import Q


@login_required
def user_booking(request):
    search_query = request.GET.get('search', '')
    filter_status = request.GET.get('filter', '')
    
    bookings = Booking.objects.filter(user=request.user)

    if search_query:
        bookings = bookings.filter(
            Q(ticket_type__name__icontains=search_query) |
            Q(ticket_type__event__name__icontains=search_query)
        )

    if filter_status:
        bookings = bookings.filter(payment_status=filter_status)

    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def booking_form(request, event_id, ticket_type_id):
    event = get_object_or_404(Event, id=event_id)
    ticket_type = get_object_or_404(TicketType, id=ticket_type_id, event=event)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.ticket_type = ticket_type
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking created!')
            return redirect('user_booking')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {
        'event': event,
        'form': form,
    })


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.user == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking canceled!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only cancel your own bookings!')
        return HttpResponseForbidden()
    return redirect(request.META.get('HTTP_REFERER', 'user_booking'))
