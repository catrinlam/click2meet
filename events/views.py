from django.shortcuts import render
from .models import EventImage
from django.shortcuts import get_object_or_404
from .models import Event


def EventListView(request):
    events = EventImage.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/event_list.html', context)


def EventDetailView(request, event_id):
    event = get_object_or_404(
        Event.objects.prefetch_related('images', 'ticket_types'),
        pk=event_id
    )
    context = {
        'event': event,
        'images': event.images.all(),
        'ticket_types': event.ticket_types.all()
    }
    return render(request, 'events/event_detail.html', context)
 