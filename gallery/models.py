from django.db import models
import datetime
import os, errno
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from testsite.settings import MEDIA_ROOT

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
        default = "sites",
        blank = True
    )

def get_image_path(instance, filename):
    slug = instance.project.slug_header
    return "projects_images/%s/%s" % (slug, filename)

class Images(models.Model):
    project = models.ForeignKey(Elements, on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name = "Галерея проекта",
        upload_to = get_image_path,
        help_text="Загрузите изображения",
        blank=True)

    def resize(self, width=None, height=None):
        img = Image.open(self.image)
        if height is None:
            basewidth = width
            width_percent = (basewidth / float(img.size[0]))
            height_size = int((float(img.size[1]) * float(width_percent)))
            resized_img = img.resize((basewidth, height_size), Image.ANTIALIAS)
        elif width is None:
            baseheight = height
            height_percent = (baseheight/ float(img.size[1]))
            width_size = int((float(img.size[0]) * float(height_percent)))
            resized_img = img.resize((width_size, baseheight), Image.ANTIALIAS)
        else:
            resized_img = ImageOps.fit(img, (width, height), Image.ANTIALIAS)
        path = MEDIA_ROOT + "/prewiew_images/%s-%s" % (width, height)
        if not os.path.exists(path):
            os.makedirs(path)
        path = path + "/%s.jpg" % self.pk
        print(path)
        resized_img.save(path)

    def save(self):

        if not self.pk or not self.image:
            super(Images, self).save()
            self.resize(width=300)
            self.resize(height=300)
            self.resize(width=900,height=220)
            self.resize(width=220, height=900)
            self.resize(width=968, height=115)





