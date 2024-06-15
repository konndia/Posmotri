from django.db import models

# Create your models here.

class Films(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    release_date = models.DateField('Дата релиза')
    image = models.ImageField('Постер', upload_to='main/static/main/img/')
    image_url = models.CharField('Ссылка', max_length=50, null=True, blank=True)
    price = models.CharField('Цена билета', max_length=5, null=True, blank=True)

    def __str__(self):
       return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class Books(models.Model):
    seanse_number = models.ForeignKey(Films, on_delete=models.PROTECT)
    seat = models.CharField('Место(-a)', max_length=50)
    mail = models.CharField('Почта', max_length=100)
    # fio = models.TextField('ФИО пользователя')

    def __str__(self):
       return f'{self.seanse_number}, место(-a) {self.seat}, почта {self.mail}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Subscribers(models.Model):
    name = models.CharField('Имя подписчика', max_length=50)
    mail = models.EmailField('Почта для подписки', max_length=100)

    def __str__(self):
       return f'{self.name}, {self.mail}'
    
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

class Sended_to_Subscribers(models.Model):
    mail = models.TextField('Сообщение', max_length=1000)

    def __str__(self):
       return f'{self.mail}'
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Seances(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    date_time = models.CharField('Дата и время', max_length=20)
    # geo = models.TextField('Расположение кинотеатра') 

    def __str__(self):
       return f'{self.title}, {self.date_time}'
    
    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'