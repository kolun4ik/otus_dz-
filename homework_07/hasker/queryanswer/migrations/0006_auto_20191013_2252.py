# Generated by Django 2.2.5 on 2019-10-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryanswer', '0005_auto_20191013_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='Url'),
        ),
    ]