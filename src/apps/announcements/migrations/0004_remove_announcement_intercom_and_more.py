# Generated by Django 5.0.3 on 2024-04-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_alter_announcementimage_announcement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='intercom',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='internet',
        ),
        migrations.AddField(
            model_name='announcement',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='bathroom',
            field=models.IntegerField(verbose_name='Ванная'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='kitchen',
            field=models.IntegerField(verbose_name='Кухня'),
        ),
    ]
