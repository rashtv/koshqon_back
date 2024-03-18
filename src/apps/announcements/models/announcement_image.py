from django.db import models

from apps.common.models.base_model import BaseModel


class AnnouncementImage(BaseModel):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['-created_at']

    announcement = models.ForeignKey(
        to='announcements.Announcement',
        verbose_name='Фотографии объявления',
        related_name='announcement_images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='media')
