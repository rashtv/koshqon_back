import base64
import io
import uuid

from PIL import Image as PILImage
from django.core.files.base import ContentFile
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.announcements.models import (
    Announcement, AnnouncementImage,
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
        # query_params = request.query_params
        announcements = Announcement.objects.filter(is_deleted=False).order_by('-created_at')

        # district = query_params.get('district', None)
        # if district:
        #     announcements = announcements.filter(district=district)
        #
        # area_gt = query_params.get('area_gt', None)
        # if area_gt:
        #     announcements = announcements.filter(area__gt=area_gt)
        #
        # area_lt = query_params.get('area_lt', None)
        # if area_lt:
        #     announcements = announcements.filter(area__lt=area_lt)
        #
        # floor_location_gt = query_params.get('floor_location_gt', None)
        # if floor_location_gt:
        #     announcements = announcements.filter(floor_location__gt=floor_location_gt)
        #
        # floor_location_lt = query_params.get('floor_location_lt', None)
        # if floor_location_lt:
        #     announcements = announcements.filter(floor_location__lt=floor_location_lt)

        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Create a new Announcement',
        request_body=AnnouncementSerializer,
        responses={201: AnnouncementSerializer()},
    )
    def post(self, request):
        request.data['user'] = request.user.id

        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            announcement = serializer.save()

            # images_data = request.data.get('images', [])
            # for image_data in images_data:
            #     image_data = base64.b64decode(image_data.get('image'))
            # image_file = io.BytesIO(image_data)
            # image = PILImage.open(image_file)

            # image_path = f'{announcement.id}.png'
            # image.save(image_path, format='PNG')
            # AnnouncementImage.objects.create(announcement=announcement, image=image_path)

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
            return Response({'message': 'Announcement does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            data=AnnouncementSerializer(announcement).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description='Update an Announcement',
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
            return Response({'message': 'Announcement does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if not request.user.id == announcement_id:
            return Response(
                {'message': 'You do not have permission to edit this announcement.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = AnnouncementSerializer(announcement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            images_data = request.FILES.getlist('images')
            for image_data in images_data:
                image = AnnouncementImage.objects.create(announcement=announcement, image_data=image_data)
            return Response(
                data=AnnouncementSerializer(announcement).data,
                status=status.HTTP_200_OK,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        operation_description='Delete an Announcement',
    )
    def delete(self, request, announcement_id):
        try:
            announcement = Announcement.objects.get(
                id=announcement_id,
                user=request.user.id,
                is_deleted=False,
            )
        except Announcement.DoesNotExist:
            return Response({'message': 'Announcement does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        announcement.is_deleted = True
        announcement.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
