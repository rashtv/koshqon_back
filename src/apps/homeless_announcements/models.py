from django.db import models

from apps.common.models.base_announcement import BaseAnnouncement


class HomelessAnnouncement(BaseAnnouncement):
    class Meta:
        verbose_name = 'Объявление без места жительства'
        verbose_name_plural = 'Объявления без места жительства'
        ordering = ['-created_at']

    user = models.CharField(
        verbose_name='Объявитель',
        max_length=255,
        blank=False,
        null=False,
        default='User'
    )
    # user = models.ForeignKey(
    #     to='User',
    #     verbose_name='Объявитель',
    #     related_name='announcement_user',
    #     on_delete=models.CASCADE,
    # )
    city = models.CharField(
        verbose_name='Город',
        max_length=255,
        blank=False,
        null=False,
    )
    district = models.CharField(
        verbose_name='Район',
        max_length=255,
        blank=False,
        null=False,
    )
    type = models.CharField(
        verbose_name='Тип места проживания',
        max_length=255,
        blank=False,
        null=False,
    )
    rooms_number = models.IntegerField(
        verbose_name='Кол-во комнат',
        blank=True,
        null=True,
    )
    floors_number = models.IntegerField(
        verbose_name='Кол-во этажей',
        blank=True,
        null=True
    )
    floor_location = models.IntegerField(
        verbose_name='Этаж расположения',
        blank=True,
        null=True,
    )
    area = models.IntegerField(
        verbose_name='Площадь',
        blank=True,
        null=True,
    )
    conditions = models.CharField(
        verbose_name='Условия',
        max_length=255,
        blank=False,
        null=False,
    )
    bathroom = models.BooleanField(
        verbose_name='Ванная',
        blank=False,
        null=False,
    )
    kitchen = models.BooleanField(
        verbose_name='Кухня',
        blank=False,
        null=False,
    )
    internet = models.BooleanField(
        verbose_name='Интернет',
        blank=False,
        null=False,
    )
    intercom = models.BooleanField(
        verbose_name='Домофон',
        blank=False,
        null=False,
    )
