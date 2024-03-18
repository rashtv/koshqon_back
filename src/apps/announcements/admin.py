from django.contrib import admin

from apps.announcements.models import (
    Announcement,
)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'district', 'street', 'house_number', 'is_deleted', ]
    list_filter = ['user', 'city', 'district', ]
