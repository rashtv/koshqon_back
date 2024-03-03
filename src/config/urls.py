from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Scema API',
        default_version='v1',
        description='Swagger Docs for Django KoshQon Backend',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='rashtv.19@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.announcements.urls', namespace='announcements')),
]
