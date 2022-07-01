from rest_framework import serializers

from recommend.models import Shoes, Brand
# from django.contrib.auth import get_user_model


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class ShoesSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)

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
