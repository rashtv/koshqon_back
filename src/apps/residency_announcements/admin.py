from django.contrib import admin

from apps.residency_announcements.models import (
    ResidencyAnnouncement,
)


@admin.register(ResidencyAnnouncement)
class ResidencyAnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'district', 'street', 'house_number', ]
    list_filter = ['user', 'city', 'district', ]
