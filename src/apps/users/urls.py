from django.urls import path
from apps.users.views import (
    FavoritesAPIView,
    FavoriteDetailAPIView, UserAnnouncementsAPIView,
)

app_name = 'users'

urlpatterns = [
    path(
        '<int:user_id>/favorites/',
        FavoritesAPIView.as_view(),
        name='list-delete-favorites'
    ),
    path(
        '<int:user_id>/favorites/<int:announcement_id>/',
        FavoriteDetailAPIView.as_view(),
        name='create-delete-favorite'
    ),
    path(
        '<int:user_id>/announcements/',
        view=UserAnnouncementsAPIView.as_view(),
        name='list-user_announcements',
    ),
]
