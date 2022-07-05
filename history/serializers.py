from multiprocessing import context
from urllib import request
from rest_framework import serializers

from .models import History, Comment
from user.models import User
from upload.models import Image

from upload.serializers import ImageSerializer
from user.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = ["user", "history", "content"]

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
        history = History(**validated_data)
        history.save()
        return history

    class Meta:
        model = History
        fields = ["id", "user", "image", "created_at",
                  "exposure_start", "exposure_end", "like"]


