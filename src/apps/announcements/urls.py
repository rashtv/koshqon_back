from django.urls import path

from apps.announcements.views import (
    AnnouncementAPIView,
    AnnouncementDetailAPIView,
)

app_name = 'announcements'

urlpatterns = [
    path(
        'announcements/',
        view=AnnouncementAPIView.as_view(),
        name='get_create_announcements',
    ),
    path(
        'announcements/<str:announcement_id>',
        view=AnnouncementDetailAPIView.as_view(),
        name='get_update_delete_announcements',
    ),
]
