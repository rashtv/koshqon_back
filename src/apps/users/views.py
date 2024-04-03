from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.announcements.models import Announcement
from apps.announcements.serializers import AnnouncementSerializer
from apps.users.models.favorite import (
    AnnouncementsFavorite,
)
from apps.users.serializers import (
    AnnouncementsFavoriteOutputSerializer,
    AnnouncementsFavoriteInputSerializer,
)


@permission_classes([permissions.IsAuthenticated])
class FavoritesAPIView(APIView):

    @swagger_auto_schema(
        operation_description='Get all Favorites Announcements',
        responses={200: AnnouncementsFavoriteOutputSerializer(many=True)},
    )
    def get(self, request, user_id):
        favorites = AnnouncementsFavorite.objects.filter(user=request.user.id)
        serializer = AnnouncementsFavoriteOutputSerializer(favorites, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description='Delete all Favorites Announcements of User',
        responses={204: 'All Favorites deleted'},
    )
    def delete(self, request, user_id):
        AnnouncementsFavorite.objects.filter(user_id=request.user.id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([permissions.IsAuthenticated])
class FavoriteDetailAPIView(APIView):

    @swagger_auto_schema(
        operation_description='Add to Favorites',
        responses={
            201: AnnouncementsFavoriteInputSerializer(),
            400: 'Announcement is already in Favorites.',
            404: 'Announcement does not exist.'
        },
    )
    def post(self, request, user_id, announcement_id):
        if AnnouncementsFavorite.objects.filter(
                user=request.user.id,
                announcement=announcement_id
        ).first():
            return Response(
                data='Announcement is already in Favorites.',
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {'user': request.user.id, 'announcement': announcement_id}
        serializer = AnnouncementsFavoriteInputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        operation_description='Delete a certain announcement from Favorites',
        responses={
            204: 'Favorite has been deleted.',
            404: 'Favorite does not exist.',
        }
    )
    def delete(self, request, user_id, announcement_id):
        favorite = AnnouncementsFavorite.objects.filter(
            user=request.user.id,
            announcement=announcement_id,
        ).first()
        if favorite:
            favorite.delete()
            return Response(
                data='Favorite has been deleted.',
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            data='Favorite does not exist.',
            status=status.HTTP_404_NOT_FOUND,
        )


@permission_classes([permissions.IsAuthenticated])
class UserAnnouncementsAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get all User Announcements',
        responses={200: AnnouncementSerializer(many=True)}
    )
    def get(self, request, user_id):
        announcements = Announcement.objects.filter(user=user_id, is_deleted=False)
        serializer = AnnouncementSerializer(instance=announcements, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
