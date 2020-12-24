from django.shortcuts import render
from . models import Event


def home(request):
    all_events = Event.objects
    return render(request, 'events/home.html', {'context_events': all_events})

