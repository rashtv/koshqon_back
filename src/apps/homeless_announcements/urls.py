from django.urls import path

from apps.homeless_announcements.views import (
    HomelessAnnouncementAPIView,
    HomelessAnnouncementDetailAPIView,
)

app_name = 'homeless_announcements'


urlpatterns = [
    path(
        'homeless_announcements/',
        view=HomelessAnnouncementAPIView.as_view(),
        name='homeless_announcements',
    ),
    path(
        'homeless_announcements/<str:announcement_id>',
        view=HomelessAnnouncementDetailAPIView.as_view(),
        name='get_update_delete_homeless_announcements',
    )
]
