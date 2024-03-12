from rest_framework import serializers

from apps.residency_announcements.models import (
    ResidencyAnnouncement,
)


class ResidencyAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidencyAnnouncement
        fields = '__all__'
        unlisted_fields = [
            'id',
            'created_at',
            'updated_at',
        ]


class ResidencyAnnouncementInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidencyAnnouncement
        fields = [
            'user', 'city', 'district', 'street', 'house_number',
            'type', 'rooms_number', 'floors_number', 'floor_location',
            'area', 'conditions',
            'bathroom', 'kitchen', 'internet', 'intercom',
        ]


class ResidencyAnnouncementOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidencyAnnouncement
        fields = '__all__'