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
    AnnouncementFilterSerializer,
)


@permission_classes([permissions.IsAuthenticated])
class AnnouncementAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Get all announcements',
        query_serializer=AnnouncementFilterSerializer(),
        responses={200: AnnouncementSerializer(many=True)},
    )
    def get(self, request):
        # query_params = request.
        query_params = request.query_params
        announcements = Announcement.objects.filter(is_deleted=False).order_by('-created_at')

        city = query_params.get('city', None)
        if city:
            announcements = announcements.filter(city=city)

        floors_number_gte = query_params.get('floors_number_gte', None)
        if floors_number_gte:
            announcements = announcements.filter(floors_number__gte=floors_number_gte)

        floors_number_lte = query_params.get('floors_number_lte', None)
        if floors_number_lte:
            announcements = announcements.filter(floors_number__lte=floors_number_lte)

        floor_location_gte = query_params.get('floor_location_gte', None)
        if floor_location_gte:
            announcements = announcements.filter(floor_location__gte=floor_location_gte)

        floor_location_lte = query_params.get('floor_location_lte', None)
        if floor_location_lte:
            announcements = announcements.filter(floor_location__lte=floor_location_lte)

        area_gte = query_params.get('area_gte', None)
        if area_gte:
            announcements = announcements.filter(area__gte=area_gte)

        area_lte = query_params.get('area_lte', None)
        if area_lte:
            announcements = announcements.filter(area__lte=area_lte)

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
