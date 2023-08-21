# Generated by Django 4.2 on 2023-05-16 00:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bouldering', '0002_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]