from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('update/<int:pk>', views.EventUpdate.as_view(), name='update'),
    path('create/', views.EventCreate.as_view(), name='create'),
    path('delete/<int:pk>', views.EventDelete.as_view(), name='delete'),
    path('stats/', views.EventStats.as_view(), name='stats'),
    path('attend/',views.attend,name='create')
]
