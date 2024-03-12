from rest_framework import serializers

from apps.homeless_announcements.models import (
    HomelessAnnouncement,
)


class HomelessAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessAnnouncement
        fields = '__all__'
        unlisted_fields = [
            'id',
            'created_at',
            'updated_at',
        ]


class HomelessAnnouncementInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessAnnouncement
        fields = [
            'user', 'city', 'district',
            'type', 'rooms_number', 'floors_number', 'floor_location',
            'area', 'conditions',
            'bathroom', 'kitchen', 'internet', 'intercom',
        ]


class HomelessAnnouncementOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessAnnouncement
        fields = '__all__'
