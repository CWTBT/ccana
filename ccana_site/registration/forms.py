from django import forms
from .models import Event
from datetime import datetime

class AttendanceForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.order_by('-start_time').reverse().filter(end_time__gt = datetime.now()))
    id = forms.IntegerField()
    name = forms.CharField(max_length=300)
    email = forms.CharField(max_length=200,required=False)
    phone = forms.CharField(max_length=20,required=False)
