from django.urls import path
from apps.users.views import (
    FavoritesAPIView,
    FavoriteDetailAPIView,
)

app_name = 'users'

urlpatterns = [
    path(
        'users/<str:user_id>/favorites/',
        FavoritesAPIView.as_view(),
        name='favorites_list_delete'
    ),
    path(
        'users/<str:user_id>/favorites/<str:announcement_id>/',
        FavoriteDetailAPIView.as_view(),
        name='favorite_post_delete'
    ),
]
