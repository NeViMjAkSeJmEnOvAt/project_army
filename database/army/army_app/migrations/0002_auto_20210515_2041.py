# Generated by Django 3.2 on 2021-05-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platoon',
            name='country',
            field=models.CharField(help_text='Zadejte misto nasazeni skupiny.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='solider',
            name='activity',
            field=models.BooleanField(help_text='Je vojak prave aktivni?', null=True),
        ),
        migrations.AddField(
            model_name='solider',
            name='rank',
            field=models.CharField(default='privateD', help_text='Zadej hodnost vojaka.', max_length=50),
        ),
        migrations.AlterField(
            model_name='platoon',
            name='leader',
            field=models.ForeignKey(on_delete=models.SET('Neurceno'), to='army_app.solider'),
        ),
    ]