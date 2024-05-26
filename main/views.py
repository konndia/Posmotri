from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/main.html')

def poster(request):
    return render(request, "main/poster.html")

def login(request):
    return render(request, "main/login.html")

def about(request):
    return render(request, "main/about.html")