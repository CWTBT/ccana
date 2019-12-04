from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Count
from .forms import AttendanceForm
from .models import Event, Attendance, User
from datetime import datetime

class IndexView(generic.ListView):
    template_name = 'registration/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
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

class EventStats(generic.base.TemplateView):
    template_name = 'registration/stats.html'
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['users'] = User.objects.all()
        context_data['event_attendance'] = Event.objects.annotate(attendees = Count('attendance'))
        return context_data

def attend(request):
   form = AttendanceForm()
   print('serving attend')
   if request.method == "POST":
      print('attendance post')
      form = AttendanceForm(request.POST)
      if form.is_valid():
          data = form.cleaned_data
          update_dict = {}
          name = data['name'].split()
          phone = data['phone']
          email = data['email']
          update_dict['id']=data['id']
          update_dict['first_name']=name[0]
          update_dict['last_name']=" ".join(name[1:])
          if (data['phone']!=''):
              update_dict['phone']=data['phone']
          if (data['email']!=''):
              update_dict['email']=data['email']
          event = data['event']
          (u,_) = User.objects.filter(pk=data['id']).update_or_create(update_dict)
          a = Attendance(user = u,event = event)
          a.save()
          return HttpResponseRedirect('/')
   errors = form.errors or None
   return render(request, 'registration/attendance_form.html',{
          'form': form,
          'errors': errors,
   })
