from rest_framework import serializers

from recommend.models import Shoes, Brand
# from django.contrib.auth import get_user_model


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class ShoesSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url

    class Meta:
        model = Shoes
        fields = [
            'id',
            'brand',
            'name',
            'color',
            'height',
            'image'
        ]
