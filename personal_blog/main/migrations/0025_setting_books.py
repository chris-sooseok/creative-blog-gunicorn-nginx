# Generated by Django 3.2.6 on 2021-08-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_setting_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='books',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
