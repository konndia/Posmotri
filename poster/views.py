from django.shortcuts import render
from .models import Films, Seances, Books, Subscribers
from .forms import SeancesForm, BooksForm, SubscribersForm, Sended_to_SubscribersForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .reminder import remind
import threading


def poster(request):
    films = Films.objects.order_by('-release_date')
    return render(request, 'main/poster.html', {'films': films})

def booking(request):
    filmss = Films.objects.all()
    bookss = Books.objects.all()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('send_email')
    else:
        form = BooksForm()
    return render(request, 'main/booking.html', {'form': form, 'filmss': filmss, 'bookss': bookss})

def foo(email_to):
    remind(email_to)
    return

def send_email(request):
    # Books.objects.last()
    last_book = Books.objects.all().last()
    email_to = [f'{last_book.mail}', ]
    send_mail("Посмотри - заказ", f"Вы заказали билет на {last_book.seanse_number}, ваше место {last_book.seat}", settings.EMAIL_HOST_USER, email_to)
    # remind(last_book.seanse_number.date_time, email_to)
    # await remind(email_to)
    # thread1 = threading.Thread(target=foo(email_to))
    # thread1.start()
    return render(request, 'main/send_email.html', {'email': email_to[0]})

class subscribe(CreateView):
    model = Books
    form_class = SubscribersForm
    template_name = 'main/subscribe.html'
    success_url = '/'

def send_to_subscribers(request):
    subs = Subscribers.objects.all()
    email_to = []
    for i in range(len(subs)):
        email_to.append(subs[i].mail)
    if request.method == 'POST':
        form = Sended_to_SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail("Посмотри - сообщение для подписчиков", f"{request.POST.get('mail')}", settings.EMAIL_HOST_USER, email_to)
            return HttpResponseRedirect('/')
    else:
        form = Sended_to_SubscribersForm()
    return render(request, 'main/send_to_subscribers.html', {'form': form})
