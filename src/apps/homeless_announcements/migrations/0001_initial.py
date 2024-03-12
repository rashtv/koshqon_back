# Generated by Django 5.0.2 on 2024-03-12 19:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomelessAnnouncement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1024)),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('district', models.CharField(max_length=255, verbose_name='Район')),
                ('type', models.CharField(max_length=255, verbose_name='Тип места проживания')),
                ('rooms_number', models.IntegerField(blank=True, null=True, verbose_name='Кол-во комнат')),
                ('floors_number', models.IntegerField(blank=True, null=True, verbose_name='Кол-во этажей')),
                ('floor_location', models.IntegerField(blank=True, null=True, verbose_name='Этаж расположения')),
                ('area', models.IntegerField(blank=True, null=True, verbose_name='Площадь')),
                ('conditions', models.CharField(max_length=255, verbose_name='Условия')),
                ('bathroom', models.BooleanField(verbose_name='Ванная')),
                ('kitchen', models.BooleanField(verbose_name='Кухня')),
                ('internet', models.BooleanField(verbose_name='Интернет')),
                ('intercom', models.BooleanField(verbose_name='Домофон')),
            ],
            options={
                'verbose_name': 'Объявление без места жительства',
                'verbose_name_plural': 'Объявления без места жительства',
                'ordering': ['-created_at'],
            },
        ),
    ]