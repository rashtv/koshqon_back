from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import (
    HomelessAnnouncement,
)
from ...serializers.homeless_announcements.serializers import (
    HomelessAnnouncementSerializer,
)


@permission_classes([permissions.IsAuthenticated])
class HomelessAnnouncementAPIView(APIView):
    @swagger_auto_schema(
        method='GET',
    )
    def get(self, request, *args, **kwargs):
        announcements = HomelessAnnouncement.objects.all().order_by('-created_at')
        serializer_class = HomelessAnnouncementSerializer(announcements, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    # def post(self, request, *args, **kwargs):
    #     serializer = HomelessAnnouncementSerializer(data=request)

