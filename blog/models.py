from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


def get_image_url(instance, filename):
    return 'Posts/images/{0}/{1}'.format(instance.user.username, filename)

class Post(models.Model):

    title = models.CharField('Название', max_length=255,)
    slug = models.SlugField('URL-кодировка')
    content = models.TextField('Содержание', max_length=5000)
    photo = models.ImageField('Фото',upload_to=get_image_url)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=User, verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    time_create = models.DateTimeField('date_published', auto_now_add=True)
    time_update = models.DateTimeField('date_update', auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PostDetail', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField('Название категории',max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('PostListCategory', kwargs={'cat_id': self.id})