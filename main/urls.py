from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    # path('booking', views.booking, name='booking')
]