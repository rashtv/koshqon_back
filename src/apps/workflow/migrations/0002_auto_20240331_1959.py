# Generated by Django 5.0.3 on 2024-03-31 14:59

from django.db import migrations

from apps.workflow.models import (
    City,
    Nationality,
)


def add_initial_data(apps, schema_editor):
    City.objects.bulk_create([
        City(name='Алматы', code='727'),
        City(name='Астана', code='7172'),
        City(name='Шымкент', code='7252'),
        City(name='Актау', code='7292'),
        City(name='Актобе', code='7132'),
        City(name='Атырау', code='7122'),
        City(name='Караганда', code='7212'),
        City(name='Кокшетау', code='7162'),
        City(name='Костанай', code='7142'),
        City(name='Павлодар', code='7182'),
        City(name='Петропавловск', code='7152'),
        City(name='Талдыкорган', code='7282'),
        City(name='Тараз', code='7262'),
        City(name='Уральск', code='7112'),
        City(name='Усть-Каменогорск', code='7232'),
        # Add more cities as needed
    ])

    Nationality.objects.bulk_create([
        Nationality(name='Казах'),
        Nationality(name='Русский'),
        Nationality(name='Уйгур'),
        Nationality(name='Татар'),
        Nationality(name='Украинец'),
        Nationality(name='Немец'),
        Nationality(name='Кореец'),
        Nationality(name='Узбек'),
        Nationality(name='Киргиз'),
        Nationality(name='Туркмен'),
        Nationality(name='Таджик'),
        Nationality(name='Китаец'),
        Nationality(name='Азербайджанец'),
        Nationality(name='Армянин'),
        Nationality(name='Грузин'),
        Nationality(name='Турок'),
        Nationality(name='Иранец'),
        Nationality(name='Латыш'),
        Nationality(name='Литовец'),
        Nationality(name='Финн'),
        Nationality(name='Венгр'),
        Nationality(name='Поляк'),
        Nationality(name='Чех'),
        Nationality(name='Словак'),
        Nationality(name='Словенец'),
        Nationality(name='Хорват'),
        Nationality(name='Серб'),
        Nationality(name='Болгар'),
        Nationality(name='Молдаванин'),
        Nationality(name='Румын'),
        Nationality(name='Грек'),
        Nationality(name='Испанец'),
        Nationality(name='Итальянец'),
        Nationality(name='Француз'),
        Nationality(name='Британец'),
        # Add more nationalities as needed
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
