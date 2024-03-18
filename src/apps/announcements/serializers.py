from rest_framework import serializers

from apps.announcements.models import (
    Announcement,
    AnnouncementImage,
)


class AnnouncementImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnnouncementImage
        fields = ('id', 'image', )


class AnnouncementSerializer(serializers.ModelSerializer):
    images = AnnouncementImageSerializer(many=True, required=False)

    class Meta:
        model = Announcement
        fields = (
            'id', 'user', 'images',
            'city', 'district', 'street', 'house_number', 'type',
            'rooms_number', 'floors_number', 'floor_location', 'area',
            'conditions', 'bathroom', 'kitchen', 'internet', 'intercom',
        )

    def get_images(self, obj):
        images = AnnouncementImage.objects.filter(announcement=obj)
        return AnnouncementImageSerializer(images, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = self.get_images(instance)
        return data

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        announcement = Announcement.objects.create(**validated_data)
        for image_data in images_data:
            AnnouncementImage.objects.create(announcement=announcement, **image_data)
        return announcement

    # def update(self, instance, validated_data):
    #     instance.images = validated_data.pop('images', [])
    #     instance.save()
    #     announcement = Announcement.objects.get(id=instance.id)
    #     announcement.update(**validated_data)
    #     announcement.save()
    #     return announcement
