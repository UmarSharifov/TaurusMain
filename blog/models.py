from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


def get_image_url(instance, filename):
    return 'Posts/images/{0}/{1}'.format(instance.user.username, filename)


class Post(models.Model):

    title = models.CharField(_('Название'), max_length=255,)
    slug = models.SlugField(_('URL-кодировка'))
    content = models.TextField(_('Содержание'), max_length=5000)
    photo = models.ImageField(_('Фото'), upload_to=get_image_url, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=User)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    time_create = models.DateTimeField(_('date_published'), auto_now_add=True)
    time_update = models.DateTimeField(_('date_update'), auto_now=True)
    is_published = models.BooleanField(_('Статус публикации'),default=True,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PostDetail', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(_('Название категории'), max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('PostListCategory', kwargs={'cat_id': self.id})


class Genre(models.Model):
    name = models.CharField(_('Жанр'), max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(_("Название"), max_length=255)
    slug = models.SlugField(_("URL"))
    content = models.TextField(_('Описание'),max_length=5000)
    photo = models.ImageField(upload_to='Movies/%Y/%M/%D')
    year = models.PositiveIntegerField(
        default=datetime.date.today().year, validators=[MinValueValidator(1984), MaxValueValidator(datetime.date.today().year)])
    country = models.CharField(_('Страна'), max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=User)
    time_create = models.DateTimeField(_('date_published'), auto_now_add=True)
    time_update = models.DateTimeField(_('date_update'), auto_now=True)
    is_published = models.BooleanField(_('Статус публикации'), default=True)

    def __str__(self):
        return self.title
