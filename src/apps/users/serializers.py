from rest_framework import serializers
from apps.users.models.favorite import (
    HomelessAnnouncementsFavorite,
    ResidencyAnnouncementsFavorite,
)


class HomelessAnnouncementsFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessAnnouncementsFavorite
        fields = '__all__'


class ResidencyAnnouncementsFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidencyAnnouncementsFavorite
        fields = '__all__'
