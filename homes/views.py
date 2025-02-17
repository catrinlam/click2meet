from django.shortcuts import render
from events.models import EventImage
from events.models import Event

def home(request):
    events = Event.objects.all().prefetch_related('images').order_by('-created_at')[:3]
    context = {
        'events': events
    }
    return render(request, 'homes/index.html', context)
