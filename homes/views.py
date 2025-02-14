from django.shortcuts import render
from events.models import EventImage

def home(request):
    events = EventImage.objects.all()
    context = {
        'events': events
    }
    return render(request, 'homes/index.html', context)
