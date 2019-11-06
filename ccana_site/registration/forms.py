from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ()
        fields = ['name', 'description','location','start_time','end_time']
