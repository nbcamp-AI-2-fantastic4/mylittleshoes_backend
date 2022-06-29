from rest_framework import serializers
from .models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['age', 'intro']

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    brand = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return "브랜드가 들어갈 자리"

    class Meta:
        model = User
        fields = ["username", "password", "fullname", "email", "userprofile", "brand"]

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        userprofile = validated_data.pop('userprofile')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        userprofile = UserProfile.objects.create(user=user, **userprofile)
        userprofile.save()

        return user   