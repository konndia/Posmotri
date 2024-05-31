from django.db import models

# Create your models here.

class Films(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    release_date = models.DateField('Дата релиза')
    image = models.ImageField('Постер', upload_to='main/static/main/img/')
    image_url = models.CharField('Ссылка', max_length=50, null=True, blank=True)

    def __str__(self):
       return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'