# Generated by Django 3.2.4 on 2021-06-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210618_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='city',
            name='icon',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='city',
            name='temperature',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
