from django.db import models

from apps.common.models.base_model import BaseModel


class HomelessAnnouncementsFavorite(BaseModel):
    class Meta:
        verbose_name = 'Список избранных объявлений без м/ж'
        verbose_name_plural = 'Списки избранных объявлений без м/ж'
        ordering = ('-created_at',)

    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
    )
    announcement = models.ForeignKey(
        to='homeless_announcements.HomelessAnnouncement',
        on_delete=models.CASCADE,
    )


class ResidencyAnnouncementsFavorite(BaseModel):
    class Meta:
        verbose_name = 'Список избранных объявлений с м/ж'
        verbose_name_plural = 'Списки избранных объявлений с м/ж'
        ordering = ('-created_at',)

    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
    )
    announcement = models.ForeignKey(
        to='residency_announcements.ResidencyAnnouncement',
        on_delete=models.CASCADE,
    )
