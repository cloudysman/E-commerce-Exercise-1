# Generated by Django 4.1.13 on 2024-01-25 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
    ]
