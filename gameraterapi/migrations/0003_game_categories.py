# Generated by Django 3.2.6 on 2021-08-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameraterapi', '0002_auto_20210811_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(related_name='attending', through='gameraterapi.GameCategory', to='gameraterapi.Category'),
        ),
    ]
