from django.shortcuts import render, get_object_or_404
from .models import EventImage, Event
from bookings.models import Booking
from bookings.forms import BookingForm
from django.db.models import Q

def EventListView(request):
    search_query = request.GET.get('search', '')
    city_filter = request.GET.get('city', '')
    date_filter = request.GET.get('date', '')

    events = Event.objects.all().prefetch_related('images').order_by('-created_at')

    if search_query:
        events = events.filter(
            Q(name__icontains=search_query) |
            Q(organizer__icontains=search_query) |
            Q(address__icontains=search_query) |
            Q(city__icontains=search_query)
        )

    if city_filter:
        events = events.filter(city__icontains=city_filter)

    if date_filter:
        events = events.filter(date=date_filter)

    context = {
        'events': events,
        'search_query': search_query,
        'city_filter': city_filter,
        'date_filter': date_filter,
    }
    return render(request, 'events/event_list.html', context)

def EventDetailView(request, event_id):
    event = get_object_or_404(
        Event.objects.all().prefetch_related('images', 'ticket_types'),
        pk=event_id
    )
    user_bookings = Booking.objects.filter(ticket_type__event=event, user=request.user)
    context = {
        'event': event,
        'images': event.images.all(),
        'ticket_types': event.ticket_types.all(),
        'form': BookingForm(),
        'user_bookings': user_bookings,
    }
    return render(request, 'events/event_detail.html', context)
