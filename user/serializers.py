import re
from rest_framework import serializers
from .models import User, UserProfile

SPECIAL_CHAR = ['`', '~', '!', '@', '#', '%', '^', '&', '*', '(', ')',
                ',', '.', '/', '<', '>', '?', '[', ']', '{', '}']


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

    def validate(self, data):
        password = data.get('password', "")

        if len(password) < 8 or len(password) > 14:
            raise serializers.ValidationError(
                    detail={"error": "비밀번호는 8글자 이상, 14글자 이하이어야합니다."},
                )

        if not any(char in SPECIAL_CHAR for char in password):
            raise serializers.ValidationError(
                    detail={"error": "특수문자가 1개이상 포함되어야합니다."},
                )

        if re.search('[0-9]+', password) is None:
            raise serializers.ValidationError(
                    detail={"error": "숫자가 1개이상 포함되어야합니다."},
                )

        if (re.search('[a-z]+', password) is None) and (re.search('[A-Z]+', password) is None):
            raise serializers.ValidationError(
                    detail={"error": "영문 대문자 또는 소문자가 1개이상 포함되어야합니다."},
                )

        return data

    def create(self, validated_data):
        userprofile = validated_data.pop('userprofile')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        userprofile = UserProfile.objects.create(user=user, **userprofile)

        return validated_data