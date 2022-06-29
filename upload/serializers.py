from rest_framework import serializers

from upload.models import Image as ImageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ["image_one", "image_two", "image_result"]
        