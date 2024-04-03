from django.urls import path

from apps.workflow.views import (
    CityAPIView,
    NationalityAPIView,
)

app_name = 'workflow'

urlpatterns = [
    path(
        'cities/',
        view=CityAPIView.as_view(),
        name='list-cities',
    ),
    path(
        'nationalities/',
        view=NationalityAPIView.as_view(),
        name='list-nationalities',
    )
]