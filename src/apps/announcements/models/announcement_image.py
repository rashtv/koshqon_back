from django.db import models

from apps.common.models.base_model import BaseModel


class AnnouncementImage(BaseModel):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['-created_at']

    announcement = models.ForeignKey(
        to='announcements.Announcement',
        to_field='id',
        verbose_name='Объявление',
        related_name='announcement_images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name='Фотография объявления',
        upload_to='media',
    )
