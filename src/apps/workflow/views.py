from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.workflow.models import City, Nationality


class CityAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retrieve list of all valid Cities',
        responses={200: 'Success'},
    )
    def get(self, request):
        cities = City.objects.all().values('name', 'code').order_by('name')
        return Response(
            data=cities,
            status=status.HTTP_200_OK,
        )


class NationalityAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retrieve list of all Nationalities',
        responses={200: 'Success'},
    )
    def get(self, request):
        nationalities = Nationality.objects.all().values('name').order_by('name')
        return Response(
            data=nationalities,
            status=status.HTTP_200_OK,
        )
