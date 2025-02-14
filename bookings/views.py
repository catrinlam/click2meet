from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from events.models import Event
from events.views import EventDetailView


@login_required
def user_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def create_booking(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user_booking = Booking.objects.filter(ticket_type__event=event, user=request.user).first()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.ticket_type = form.cleaned_data['ticket_type']
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking created!')
            return redirect('EventDetailView', event_id=event.id)
    else:
        form = BookingForm()
        if user_booking:
            messages.add_message(request, messages.ERROR, 'You can only book one ticket per event!')
    return render(request, 'bookings/create_booking.html', {
        'event': event,
        'form': form,
        'user_booking': user_booking,
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
    return redirect('user_booking')
