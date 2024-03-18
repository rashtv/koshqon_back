from django.contrib import admin

from apps.announcements.models import (
    Announcement,
    AnnouncementImage,
)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'district', 'street', 'house_number', 'is_deleted', ]
    list_filter = ['user', 'city', 'district', ]


@admin.register(AnnouncementImage)
class AnnouncementImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'announcement', 'image', 'created_at', ]
    list_filter = ['announcement', ]
