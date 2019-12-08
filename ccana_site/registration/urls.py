from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('stats/', staff_member_required(views.EventStats.as_view()), name='stats'),
    path('attend/',views.attend,name='attend')
]
