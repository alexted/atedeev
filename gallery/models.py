from django.db import models
import datetime

# Create your models here.
class Elements(models.Model):
    preview_image = models.ImageField(
        verbose_name="Превью-Картинка",
        upload_to="preview_images/%Y/%m/%d",
        help_text="Загрузите изображение",
        blank=True)
    header = models.CharField(verbose_name="Заголовок",max_length=300, blank=True)
    slug_header = models.SlugField(max_length=300, blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    url = models.CharField(verbose_name="Адрес сайта",blank=True, max_length=300)
    date_time = models.DateTimeField(verbose_name="Дата", default=datetime.datetime.now)
    category_choices = (
        ("sites", 'Сайты'),
        ("games", 'Игры'),
        ("software", 'Софт'),
    )
    category = models.CharField(
        verbose_name="Категория",
        max_length = 30,
        choices = category_choices,
        default="sites",
        blank=True
    )
