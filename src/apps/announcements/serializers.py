from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from apps.announcements.models import (
    Announcement,
    AnnouncementImage,
)


class AnnouncementImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = AnnouncementImage
        fields = ('image', )

    def save(self, announcement, *args, **kwargs):
        image = AnnouncementImage.objects.create(announcement=announcement, image=self)
        return image


class AnnouncementSerializer(serializers.ModelSerializer):
    images = AnnouncementImageSerializer(many=True, required=False, allow_null=True)

    house_number = serializers.IntegerField(min_value=1, max_value=1024)
    rooms_number = serializers.IntegerField(min_value=1, max_value=1024)
    floors_number = serializers.IntegerField(min_value=1, max_value=1024)
    floor_location = serializers.IntegerField(min_value=1, max_value=1024)
    area = serializers.IntegerField(min_value=1, max_value=1024)
    kitchen = serializers.IntegerField(min_value=1, max_value=1024)
    bathroom = serializers.IntegerField(min_value=1, max_value=1024)

    class Meta:
        model = Announcement
        fields = (
            'id', 'user', 'images',
            'city', 'district', 'street', 'house_number', 'type',
            'rooms_number', 'floors_number', 'floor_location', 'area',
            'conditions', 'bathroom', 'kitchen', 'description',
        )

    def get_images(self, obj): # noqa
        images = AnnouncementImage.objects.filter(announcement=obj)
        return AnnouncementImageSerializer(images, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = self.get_images(instance)
        return data

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        announcement = Announcement.objects.create(**validated_data)
        for image_data in images_data:
            AnnouncementImage.objects.create(announcement=announcement, image=image_data.get('image'))
        return announcement

    def validate(self, validated_data):
        floors_number = validated_data.get('floors_number')
        floor_location = validated_data.get('floor_location')

        if floors_number < floor_location:
            raise serializers.ValidationError('Floor location must be less than or equal to floors number')
        return validated_data
