from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse("<h1>About us</h1>")

def login(request):
    return HttpResponse("<h1>Login</h1>")

def contact(request): 
    return HttpResponse("<h1>Contact us</h1>")