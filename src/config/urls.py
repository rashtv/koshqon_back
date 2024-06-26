from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.announcements.urls import urlpatterns as announcements_urlpatterns
from apps.users.urls import urlpatterns as users_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title='Schema API',
        default_version='v1',
        description='Swagger Docs for Django KoshQon Backend',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='rashtv.19@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

# api_urlpatterns = [
#     path('', include(
#         'apps.announcements.urls',
#         namespace='announcements',
#     )),
#     path('', include(
#         'apps.users.urls',
#         namespace='users',
#     )),
# ]

workflow_urlpatterns = [
    path('', include(
        'apps.workflow.urls',
        namespace='workflow',
    )),
]

urlpatterns = [
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'), # noqa
    path('admin/', admin.site.urls, name='admin'),
    path('announcements/', include(announcements_urlpatterns), name='announcements'),
    path('users/', include(users_urlpatterns), name='users'),
    path('workflow/', include(workflow_urlpatterns), name='workflow')
]
