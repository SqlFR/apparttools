# Generated by Django 5.0.6 on 2024-05-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_arrangement', '0005_apartment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='slug',
            field=models.SlugField(default='', max_length=32),
        ),
    ]
