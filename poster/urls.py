from django.urls import path
from . import views
from .views import booking, subscribe

urlpatterns = [
    path('afisha', views.poster, name='afisha'),
    path('afisha', views.poster, name='poster'),
    path('booking', views.booking, name='booking'),
    path('send_email', views.send_email, name='send_email'),
    path('subscribe', subscribe.as_view(), name='subscribe'),
    path('send_to_subscribers', views.send_to_subscribers, name='send_to_subscribers')
]