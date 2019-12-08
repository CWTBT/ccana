from django.urls import path
from home import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parents', views.parents, name='parents'),
    path('providers', views.providers, name='providers'),
    path('staff', views.staff, name='staff'),
    path('sponsors', views.sponsors, name="sponsors"),
    path('contact_us', views.contact, name='contact_us'),
]
