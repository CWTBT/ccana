from django.contrib import admin
from registration.models import Event, User, Attendance
from django.http import HttpResponseRedirect

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Attendance)
