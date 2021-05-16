# Generated by Django 3.2 on 2021-05-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army_app', '0008_auto_20210516_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranks',
            name='score',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='solider',
            name='rank',
            field=models.ForeignKey(default='1', on_delete=models.SET('Vojín'), to='army_app.ranks'),
        ),
    ]
