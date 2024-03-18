from django.db import models

from apps.common.models.base_model import BaseModel


class AnnouncementsFavorite(BaseModel):
    class Meta:
        verbose_name = 'Список избранных объявлений'
        verbose_name_plural = 'Списки избранных объявлений'
        ordering = ('-created_at',)

    user = models.ForeignKey(
        to='users.User',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    announcement = models.ForeignKey(
        to='announcements.Announcement',
        verbose_name='Объявление',
        on_delete=models.CASCADE,
    )
