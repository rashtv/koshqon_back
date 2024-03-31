from django.contrib import admin
from apps.workflow.models import (
    City,
    Nationality,
)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', ]
    list_filter = ['id', 'name', 'code', ]
    search_fields = ['name', ]


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
