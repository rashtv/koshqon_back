from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models.favorite import (
    AnnouncementsFavorite,
)
from apps.users.serializers import (
    AnnouncementsFavoriteSerializer,
)


class FavoritesAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get all Favorites Announcements',
        responses={200: AnnouncementsFavoriteSerializer(many=True)},
    )
    def get(self, request, user_id):
        favorites = AnnouncementsFavorite.objects.filter(user_id=request.user.id)
        serializer = AnnouncementsFavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description='Add to Favorites',
        request_body=AnnouncementsFavoriteSerializer,
        responses={201: AnnouncementsFavoriteSerializer()},
    )
    def post(self, request, user_id):
        serializer = AnnouncementsFavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


@permission_classes([permissions.IsAuthenticated])
class FavoriteDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Delete a certain announcement from Favorites',
    )
    def delete(self, request, user_id, announcement_id):
        favorite = AnnouncementsFavorite.objects.filter(
            user=user_id,
            announcement=announcement_id,
        )
        if favorite.first():
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
