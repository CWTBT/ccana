from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Event
from datetime import datetime

class IndexView(generic.ListView):
    template_name = 'registration/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by('-start_time').reverse().filter(end_time__gt = datetime.now())

class EventCreate(generic.edit.CreateView):
    model = Event
    fields = ['name', 'description','location','start_time','end_time']
    success_url = '/registration'

class EventUpdate(generic.edit.UpdateView):
    model = Event
    fields = ['name', 'description','location','start_time','end_time']
    template_name_suffix = '_update_form'
    success_url = '/registration'

class EventDelete(generic.edit.DeleteView):
    model = Event
    success_url = '/registration'
