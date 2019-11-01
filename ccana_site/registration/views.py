from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Event
from .forms import EventForm

class IndexView(generic.ListView):
    template_name = 'registration/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by('-start_time').reverse()


def create(request):
    if (request.method=='POST'):
        form = EventForm(request.POST)
        print("processing post")
        print(reverse('registration:index'))
        e = form.save(commit=False)
        e.save();
        return HttpResponseRedirect(reverse('registration:index'))
    else:
        print("create serving non-post");
        form = EventForm();
        return render(request, 'registration/create.html',{'form':form})
