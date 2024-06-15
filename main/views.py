from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def main(request):
    return HttpResponseRedirect('poster/afisha')

def about(request):
    try:
        User.objects.create_superuser('admin', '', '12345678')
    finally:
        return render(request, "main/about.html")

# def booking(request):
#     return render(request, "main/booking.html")
