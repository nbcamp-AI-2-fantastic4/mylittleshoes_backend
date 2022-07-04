from multiprocessing import context
from urllib import request
from rest_framework import serializers

from .models import History, Comment
from user.models import User
from upload.models import Image

from upload.serializers import ImageSerializer
from user.serializers import UserSerializer

# 히스토리 시리얼라이저
class HistorySerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField()
    image = ImageSerializer(read_only=True)
    like = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        return obj.user.username
    
    def get_like(self, obj):
        like_count = obj.like_set.count()
        return like_count

    def create(self, validated_data):
        # image = Image.objects.last()
        history = History(**validated_data)
        history.save()
        return history
        # return History()

    class Meta:
        model = History
        fields = ["user", "image", "created_at",
                  "exposure_start", "exposure_end", "like"]


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        return obj.user.username

    def get_image(self, obj):
        images = {}
        image_one = str(obj.history.image.image_one)
        image_two = str(obj.history.image.image_two)
        image_result = str(obj.history.image.image_result)
        images['image_one'] = image_one
        images['image_two'] = image_two
        images['image_result'] = image_result
        
        return images

    class Meta:
        model = Comment
        fields = ["user", "history", "content", "image"]