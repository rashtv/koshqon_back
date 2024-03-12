from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.residency_announcements.models import (
    ResidencyAnnouncement,
)
from apps.residency_announcements.serializers import (
    ResidencyAnnouncementSerializer,
    ResidencyAnnouncementInputSerializer,
    ResidencyAnnouncementOutputSerializer,
)


@permission_classes([permissions.IsAuthenticated])
class ResidencyAnnouncementAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get all Residency Announcements',
        responses={200: ResidencyAnnouncementOutputSerializer(many=True)},
    )
    def get(self, request):
        announcements = ResidencyAnnouncement.objects.filter(is_deleted=False).order_by('-created_at')
        serializer = ResidencyAnnouncementOutputSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Create a new Residency Announcement',
        request_body=ResidencyAnnouncementInputSerializer,
        responses={201: ResidencyAnnouncementOutputSerializer()},
    )
    def post(self, request):
        serializer = ResidencyAnnouncementInputSerializer(data=request.data)
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
class ResidencyAnnouncementDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get a specific Residency Announcement',
        responses={200: ResidencyAnnouncementOutputSerializer()}
    )
    def get(self, request, announcement_id):
        try:
            announcement = ResidencyAnnouncement.objects.get(
                id=announcement_id,
                is_deleted=False
            )
        except ResidencyAnnouncement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(
            data=ResidencyAnnouncementOutputSerializer(announcement).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description='Update a Residency Announcement',
        request_body=ResidencyAnnouncementInputSerializer,
        responses={200: ResidencyAnnouncementOutputSerializer()},
    )
    def patch(self, request, announcement_id):
        try:
            announcement = ResidencyAnnouncement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except ResidencyAnnouncement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ResidencyAnnouncementInputSerializer(
            announcement,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=ResidencyAnnouncementOutputSerializer(announcement).data,
                status=status.HTTP_200_OK,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        operation_description='Delete an existing Residency Announcement',
    )
    def delete(self, request, announcement_id):
        try:
            announcement = ResidencyAnnouncement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except ResidencyAnnouncement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        announcement.is_deleted = True
        announcement.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
