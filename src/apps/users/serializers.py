from rest_framework import serializers
from apps.users.models.favorite import (
    AnnouncementsFavorite,
)


class AnnouncementsFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementsFavorite
        fields = '__all__'
