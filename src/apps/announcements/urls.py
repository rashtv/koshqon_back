from django.urls import path

from apps.announcements.views import (
    AnnouncementAPIView,
    AnnouncementDetailAPIView,
)

app_name = 'announcements'

urlpatterns = [
    path(
        '',
        view=AnnouncementAPIView.as_view(),
        name='list-create-announcements',
    ),
    path(
        '<int:announcement_id>/',
        view=AnnouncementDetailAPIView.as_view(),
        name='read-update-delete-announcements',
    ),
]
