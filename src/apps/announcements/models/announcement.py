from django.db import models

from apps.common.models.base_model import BaseModel
from apps.common.models.soft_delete_model import SoftDeleteModel


class Announcement(BaseModel, SoftDeleteModel):
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    user = models.ForeignKey(
        to='users.User',
        to_field='id',
        verbose_name='Объявитель',
        related_name='announcement_user',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
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
    street = models.CharField(
        verbose_name='Улица',
        max_length=255,
        blank=False,
        null=False,
    )
    house_number = models.IntegerField(
        verbose_name='Номер дома',
        blank=False,
        null=False,
    )
    type = models.CharField(
        verbose_name='Тип места проживания',
        max_length=255,
        blank=True,
        null=True,
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
        blank=True,
        null=True,
    )
    bathroom = models.IntegerField(
        verbose_name='Ванная',
        blank=True,
        null=True,
    )
    kitchen = models.IntegerField(
        verbose_name='Кухня',
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=1023,
        blank=True,
        null=True,
    )
