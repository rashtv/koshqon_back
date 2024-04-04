import base64

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.announcements.models import (
    Announcement,
    AnnouncementImage,
)
from apps.announcements.serializers import (
    AnnouncementSerializer,
)


@permission_classes([permissions.IsAuthenticated])
class AnnouncementAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get all announcements',
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
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description='Create a new Announcement',
        request_body=AnnouncementSerializer,
        responses={201: AnnouncementSerializer()},
    )
    def post(self, request):
        request.data['user'] = request.user.id

        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            images_data = request.data.get('images', [])
            for image_data in images_data:
                base64.b64decode(image_data.get('image'))

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
        operation_description='Get the announcement',
        responses={200: AnnouncementSerializer()}
    )
    def get(self, request, announcement_id):
        try:
            announcement = Announcement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except Announcement.DoesNotExist: # noqa
            return Response(
                data={'message': 'Announcement does not exist.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            data=AnnouncementSerializer(announcement).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_description='Update the announcement',
        request_body=AnnouncementSerializer,
        responses={200: AnnouncementSerializer()},
    )
    def patch(self, request, announcement_id):
        try:
            announcement = Announcement.objects.get(
                id=announcement_id,
                is_deleted=False,
            )
        except Announcement.DoesNotExist: # noqa
            return Response(
                data={'message': 'Announcement does not exist.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not request.user.id == request.data.get('user'):
            return Response(
                data={'message': 'You do not have permission to edit this announcement.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = AnnouncementSerializer(announcement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            images_data = request.FILES.getlist('images')
            for image_data in images_data:
                AnnouncementImage.objects.create(announcement=announcement, image_data=image_data)
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
            announcement = Announcement.objects.get(id=announcement_id)
        except Announcement.DoesNotExist: # noqa
            return Response(
                data={'message': 'Announcement does not exist.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not announcement.user == request.user.id:
            return Response(
                data={'message': 'You do not have permission to delete this announcement.'},
                status=status.HTTP_403_FORBIDDEN,
            )
        if announcement.is_deleted:
            return Response(
                data={'message': 'Announcement already deleted.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        announcement.is_deleted = True
        announcement.save()

        return Response(
            data={'message': 'Announcement has been deleted.'},
            status=status.HTTP_204_NO_CONTENT,
        )
