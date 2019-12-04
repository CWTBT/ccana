from django import forms
from .models import Event
from datetime import datetime
from django.core import validators


class AttendanceForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.order_by('-start_time').reverse().filter(end_time__gt = datetime.now()),empty_label=None)
    id = forms.IntegerField()
    name = forms.CharField(max_length=300)
    email = forms.CharField(max_length=200,required=False,validators=[validators.validate_email])
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=False,
        error_messages = {"invalid":"Please enter your phone number with no punctuation. It should be between 9 and 15 digits long."})
