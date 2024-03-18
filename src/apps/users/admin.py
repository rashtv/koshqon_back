from django.contrib import admin

from apps.users.models import User
from apps.users.models.favorite import (
    AnnouncementsFavorite,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'first_name', 'last_name',]
    list_filter = []
    search_fields = ['phone_number', ]


@admin.register(AnnouncementsFavorite)
class HomelessAnnouncementsFavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'announcement', 'created_at',]
    list_filter = ['user', 'created_at',]
