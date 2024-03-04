from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.homeless_announcements.models import (
    HomelessAnnouncement,
)
from apps.homeless_announcements.serializers import (
    HomelessAnnouncementSerializer,
    HomelessAnnouncementOutputSerializer,
    HomelessAnnouncementInputSerializer,
)


@permission_classes([permissions.IsAuthenticated])
class HomelessAnnouncementAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get all Homeless Announcements',
        responses={200: HomelessAnnouncementOutputSerializer(many=True)},
    )
    def get(self, request):
        announcements = HomelessAnnouncement.objects.filter(is_deleted=False).order_by('-created_at')
        serializer = HomelessAnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Create a new Homeless Announcement',
        request_body=HomelessAnnouncementInputSerializer,
        responses={201: HomelessAnnouncementOutputSerializer()},
    )
    def post(self, request):
        serializer = HomelessAnnouncementInputSerializer(data=request.data)
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
class HomelessAnnouncementDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get a specific Homeless Announcement',
        responses={200: HomelessAnnouncementOutputSerializer()},
    )
    def get(self, request, announcement_id):
        try:
            announcement = HomelessAnnouncement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except HomelessAnnouncement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(
            data=HomelessAnnouncementOutputSerializer(announcement).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description='Update a Homeless Announcement',
        request_body=HomelessAnnouncementInputSerializer,
        responses={200: HomelessAnnouncementOutputSerializer()},
    )
    def patch(self, request, announcement_id):
        try:
            announcement = HomelessAnnouncement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except HomelessAnnouncement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = HomelessAnnouncementInputSerializer(
            announcement,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=HomelessAnnouncementOutputSerializer(announcement).data,
                status=status.HTTP_200_OK,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        operation_description='Delete an existing Homeless Announcement',
    )
    def delete(self, request, announcement_id):
        try:
            announcement = HomelessAnnouncement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except HomelessAnnouncement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        announcement.is_deleted = True
        announcement.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
