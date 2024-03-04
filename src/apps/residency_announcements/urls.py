from django.urls import path

from apps.residency_announcements.views import (
    ResidencyAnnouncementAPIView,
    ResidencyAnnouncementDetailAPIView,
)

app_name = 'residency_announcements'

urlpatterns = [
    path(
        'residency_announcements/',
        view=ResidencyAnnouncementAPIView.as_view(),
        name='get_create_residency_announcements',
    ),
    path(
        'residency_announcements/<str:announcement_id>',
        view=ResidencyAnnouncementDetailAPIView.as_view(),
        name='get_update_delete_residency_announcements',
    ),
]
