# Generated by Django 3.2.6 on 2021-08-26 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_setting_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='books',
        ),
    ]
