# Generated by Django 3.0.10 on 2020-11-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20201127_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestep',
            name='feels_like_temperature',
            field=models.IntegerField(verbose_name='Feels like'),
        ),
        migrations.AlterField(
            model_name='timestep',
            name='humidity',
            field=models.IntegerField(verbose_name='Humidity'),
        ),
        migrations.AlterField(
            model_name='timestep',
            name='temperature',
            field=models.IntegerField(verbose_name='Temperature'),
        ),
    ]