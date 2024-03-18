from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.announcements.models import (
    Announcement,
)
from apps.announcements.serializers import (
    AnnouncementSerializer,
)


@permission_classes([permissions.IsAuthenticated])
class AnnouncementAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get all Announcements',
        responses={200: AnnouncementSerializer(many=True)},
    )
    def get(self, request):
        announcements = Announcement.objects.filter(is_deleted=False).order_by('-created_at')
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Create a new Announcement',
        request_body=AnnouncementSerializer,
        responses={201: AnnouncementSerializer()},
    )
    def post(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


@permission_classes([permissions.IsAuthenticated])
class AnnouncementDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get a specific Announcement',
        responses={200: AnnouncementSerializer()}
    )
    def get(self, request, announcement_id):
        try:
            announcement = Announcement.objects.get(
                id=announcement_id,
                is_deleted=False
            )
        except Announcement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(
            data=AnnouncementSerializer(announcement).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description='Update a Announcement',
        request_body=AnnouncementSerializer,
        responses={200: AnnouncementSerializer()},
    )
    def patch(self, request, announcement_id):
        try:
            announcement = Announcement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except Announcement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AnnouncementSerializer(
            announcement,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=AnnouncementSerializer(announcement).data,
                status=status.HTTP_200_OK,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        operation_description='Delete an existing Announcement',
    )
    def delete(self, request, announcement_id):
        try:
            announcement = Announcement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except Announcement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        announcement.is_deleted = True
        announcement.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
