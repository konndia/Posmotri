from django.urls import path
from . import views

urlpatterns = [
    path('', views.poster, name='poster'),
    path('booking', views.booking, name='booking')
]