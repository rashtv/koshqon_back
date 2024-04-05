import base64

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
        image_data = self.validated_data.get('image')
        image = AnnouncementImage.objects.create(announcement=announcement, image=image_data)
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
        images = []
        images_data = AnnouncementImage.objects.filter(announcement=obj)
        for image_data in images_data:
            with open(image_data.image.name, 'rb') as image_file:
                data = image_file.read()
                images.append({
                    'image': base64.b64encode(data).decode('utf-8')
                })
        return images

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = self.get_images(instance)
        print(data.get('images'))
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
            raise serializers.ValidationError('Floor location must be less than or equal to floors number.')
        return validated_data


class AnnouncementFilterSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    type = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    rooms_number = serializers.IntegerField(min_value=1, max_value=1024, required=False, allow_null=True)
    floors_number_lte = serializers.IntegerField(min_value=1, max_value=1024, required=False, allow_null=True)
    floors_number_gte = serializers.IntegerField(min_value=1, max_value=1024, required=False, allow_null=True)
    floor_location_lte = serializers.IntegerField(min_value=1, max_value=1024, required=False, allow_null=True)
    floor_location_gte = serializers.IntegerField(min_value=1, max_value=1024, required=False, allow_null=True)
    area_lte = serializers.IntegerField(min_value=1, max_value=1024, required=False, allow_null=True)
    area_gte = serializers.IntegerField(min_value=1, max_value=1024, required=False, allow_null=True)
    conditions = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)

    def validate(self, validated_data):
        floors_number_lte = validated_data.get('floors_number_lte', None)
        floors_number_gte = validated_data.get('floors_number_gte', None)
        floor_location_lte = validated_data.get('floor_location_lte', None)
        floor_location_gte = validated_data.get('floor_location_gte', None)
        area_lte = validated_data.get('area_lte', None)
        area_gte = validated_data.get('area_gte', None)

        if floors_number_lte and floors_number_gte:
            if floors_number_lte < floors_number_gte:
                raise serializers.ValidationError(
                    'Minimal floor number must be less than or equal to maximum floor number.'
                )
        if floor_location_lte and floor_location_gte:
            if floor_location_lte < floor_location_gte:
                raise serializers.ValidationError(
                    'Minimal floor location must be less than or equal to floor location gt.'
                )
        if area_lte and area_gte:
            if area_lte > area_gte:
                raise serializers.ValidationError(
                    'Minimal area must not be less than or equal to maximal area.'
                )
        return validated_data
