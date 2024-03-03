from django.urls import path

from apps.announcements.api.residency_announcements.views import (
    ResidencyAnnouncementAPIView, ResidencyAnnouncementDetailAPIView,
)
from apps.announcements.api.homeless_announcements.views import (
    HomelessAnnouncementAPIView,
)

app_name = 'announcements'

residency_announcements_urlpatterns = [
    path(
        'residency_announcements/',
        view=ResidencyAnnouncementAPIView.as_view(),
        name='get_create_residency_announcements'
    ),
    path(
        'residency_announcements/<str:announcement_id>',
        view=ResidencyAnnouncementDetailAPIView.as_view(),
        name='get_update_delete_residency_announcements'
    ),
]

homeless_announcements_urlpatterns = [
    path(
        'homeless_announcements/',
        view=HomelessAnnouncementAPIView.as_view(),
        name='homeless_announcements'
    ),
]

urlpatterns = residency_announcements_urlpatterns + homeless_announcements_urlpatterns
