from rest_framework import serializers

from apps.announcements.models import (
    Announcement,
)


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        unlisted_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
