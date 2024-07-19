from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "profile_image",
        ]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"], email=validated_data.get("email", "")
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class ImageModelSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ImageModel
        fields = "__all__"


class ImageLikeDislikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    image = ImageModelSerializer()

    class Meta:
        model = ImageLikeDislike
        fields = "__all__"


class ImageCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    image = ImageModelSerializer()

    class Meta:
        model = ImageComment
        fields = "__all__"
