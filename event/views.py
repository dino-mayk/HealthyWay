from django.shortcuts import render

from event.models import Event


def list(request):
    template_name = 'event/list.html'

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, template_name, context)


def detail(request, pk):
    template_name = 'event/detail.html'
    event = Event.objects.get(pk=pk)
    event_schedule = event.schedule.split('\n')

    context = {
        'event': event,
        'event_schedule': event_schedule,
    }

    return render(request, template_name, context)
