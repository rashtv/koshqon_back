from django.urls import path
from apps.users.views import (
    FavoritesAPIView,
    FavoriteDetailAPIView,
)

app_name = 'users'

urlpatterns = [
    path(
        'user/<str:user_id>/favorites/',
        FavoritesAPIView.as_view(),
        name='favorites-list-add'
    ),
    path(
        'user/<str:user_id>/favorites/<str:announcement_id>/',
        FavoriteDetailAPIView.as_view(),
        name='favorite-delete'
    ),
]
