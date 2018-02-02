from django.db import models
import datetime
import os
from pathlib import Path
from PIL import Image, ImageOps
from django.conf import settings
from django.utils.html import mark_safe

# Create your models here.
class Project(models.Model):
    preview_screenshot = models.ImageField(
        verbose_name="Превью-Картинка",
        upload_to="Gallery/Project/preview_screenshot/%Y/%m/%d",
        help_text="Загрузите изображение",
        blank=True)
    header = models.CharField(verbose_name="Заголовок",max_length=300, blank=True)
    slug_header = models.SlugField(max_length=300, blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    url = models.URLField(verbose_name="Адрес сайта",blank=True)
    creation_date_time = models.DateTimeField(verbose_name="Дата", default=datetime.datetime.now)
    category_choices = (
        ("sites", 'Сайты'),
        ("games", 'Игры'),
        ("software", 'Софт'),
    )
    category = models.CharField(
        verbose_name="Категория",
        max_length=30,
        choices=category_choices,
        default="sites",
        blank=True
    )

    def resize_image(self, width=None, height=None, type = 'jpg', qual = 90):
        img = Image.open(self.preview_screenshot)
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
        path = settings.MEDIA_ROOT + "Gallery/Project/preview_screenshot/resize_image/%s-%s" % (width, height)
        if not os.path.exists(path):
            os.makedirs(path)
        path = path + "/%s.%s" % (self.pk, type)
        if type == 'jpg':
            resized_img.convert('RGB').save(path, quality=qual)
        else:
            resized_img.convert('RGB').save(path)

    def save(self):

        if not self.pk or not self.preview_screenshot:
            super(Project, self).save()
            self.resize_image(width=200)


    def get_resized_screenshot_url(self, width=None, height=None, type = 'jpg' ):
        imgpath = "Gallery/Project/preview_screenshot/resize_image/%s-%s/%s.%s" % (width, height, self.pk, type)
        file = Path(settings.MEDIA_ROOT+imgpath)
        original_img = Path(settings.BASE_DIR + self.preview_screenshot.url)
        print(original_img)
        if self.preview_screenshot and (original_img).exists():
            if file.exists():
                return settings.MEDIA_URL+imgpath
            else:
                self.resize_image(width,height,type)
                return settings.MEDIA_URL+imgpath
        else:
            return ''

    def get_resized_screenshot_200(self):
        return self.get_resized_screenshot_url(width=200)

    def get_resized_screenshot_300(self):
        return self.get_resized_screenshot_url(width=300)

    class Meta():
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

def get_image_path(instance, filename):
    slug = instance.project.slug_header
    return "projects_images/%s/%s" % (slug, filename)

class Video(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    video = models.URLField(verbose_name="Видео", blank=True)

class Screenshot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name = "Галерея проекта",
        upload_to = "Gallery/Project/Screenshot/image/%Y/%m/%d",
        help_text="Загрузите изображения",
        blank=True)

    def resize_image(self, width=None, height=None, type = 'jpg', qual = 90):
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
        path = settings.MEDIA_ROOT + "Gallery/Project/Screenshot/resize_image/%s-%s" % (width, height)
        if not os.path.exists(path):
            os.makedirs(path)
        path = path + "/%s.%s" % (self.pk, type)
        if type == 'jpg':
            resized_img.convert('RGB').save(path, quality=qual)
        else:
            resized_img.convert('RGB').save(path)

    def save(self):
        if not self.pk or not self.image:
            super(Screenshot, self).save()
            self.resize_image(width=300)
            self.resize_image(width=None, height=300)
            self.resize_image(width=900,height=220)
            self.resize_image(width=220, height=900)
            self.resize_image(width=968, height=115)

    def get_resized_screenshot_url(self, width=None, height=None, type='jpg'):
        imgpath = "Gallery/Project/Screenshot/resize_image/%s-%s/%s.%s" % (width, height, self.pk, type)
        file = Path(settings.MEDIA_ROOT+imgpath)
        if file.exists():
            return settings.MEDIA_URL+imgpath
        else:
            self.resize_image(width,height,type)
            return settings.MEDIA_URL+imgpath

    def get_resized_screenshot_url_200(self):
        return self.get_resized_screenshot_url(width=200)

    def get_resized_screenshot_url_300(self):
        return self.get_resized_screenshot_url(width=300)