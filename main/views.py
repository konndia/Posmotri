from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/main.html')

def login(request):
    return render(request, "main/login.html")

def about(request):
    return render(request, "main/about.html")

# def booking(request):
#     return render(request, "main/booking.html")