from rest_framework import serializers

from apps.announcements.models.announcements import (
    HomelessAnnouncement,
)


class HomelessAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessAnnouncement
        fields = '__all__'
