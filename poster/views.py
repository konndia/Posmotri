from django.shortcuts import render
from .models import Films

def poster(request):
    films = Films.objects.order_by('-release_date')
    return render(request, 'main/poster.html', {'films': films})

def booking(request):
    return render(request, 'main/booking.html', {'booking': booking})
