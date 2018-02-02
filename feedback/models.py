from django.db import models
import datetime

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(verbose_name="Имя", blank = True, max_length=300)
    phone = models.CharField(verbose_name='Номер телефона', blank= True, max_length=300)
    email = models.EmailField(verbose_name= "Электронная почта", blank = True)
    organization = models.CharField(verbose_name="Организация", blank= True, max_length=300)
    message = models.TextField(verbose_name="Сообщение")
    datetime = models.DateTimeField(verbose_name="Дата", default=datetime.datetime.now)
    ip = models.GenericIPAddressField(verbose_name="IP адрес", null=True ,blank=True)

    class Meta():
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
