# Generated by Django 4.1.5 on 2023-01-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_movie_year_alter_movie_user_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(default=1, max_length=255, verbose_name='Страна'),
            preserve_default=False,
        ),
    ]
