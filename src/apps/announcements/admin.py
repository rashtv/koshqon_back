from django.contrib import admin

from apps.announcements.models import (
    ResidencyAnnouncement,
    HomelessAnnouncement,
)


@admin.register(ResidencyAnnouncement)
class ResidencyAnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'district', 'street', 'house_number', ]
    list_filter = ['user', 'city', 'district', ]


@admin.register(HomelessAnnouncement)
class HomelessAnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'district', ]
    list_filter = ['user', 'city', 'district', ]
