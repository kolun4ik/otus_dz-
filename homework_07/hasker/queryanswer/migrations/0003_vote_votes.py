# Generated by Django 2.2.5 on 2019-10-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryanswer', '0002_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
