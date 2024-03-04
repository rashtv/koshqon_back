from django.contrib import admin

from apps.homeless_announcements.models import (
    HomelessAnnouncement,
)


@admin.register(HomelessAnnouncement)
class HomelessAnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'district', ]
    list_filter = ['user', 'city', 'district', ]
