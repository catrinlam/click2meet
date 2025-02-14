from django.shortcuts import render


def EventListView(request):
    return render(request, 'events/event_list.html')


def EventDetailView(request, event_id):
    return render(request, 'events/event_detail.html')