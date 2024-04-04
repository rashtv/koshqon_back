from rest_framework import serializers

from apps.announcements.serializers import AnnouncementSerializer
from apps.users.models.favorite import (
    AnnouncementsFavorite,
)


class AnnouncementsFavoriteOutputSerializer(serializers.ModelSerializer):
    announcement = AnnouncementSerializer()

    class Meta:
        model = AnnouncementsFavorite
        fields = '__all__'


class AnnouncementsFavoriteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementsFavorite
        fields = '__all__'
