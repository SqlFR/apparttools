# Generated by Django 5.0.6 on 2024-06-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_arrangement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentissues',
            name='modal',
            field=models.FloatField(default=1, verbose_name='modal'),
        ),
    ]