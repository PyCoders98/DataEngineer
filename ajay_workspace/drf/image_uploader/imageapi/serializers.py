from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
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
    user = UserSerializer(read_only=True)

    class Meta:
        model = ImageModel
        fields = "__all__"

    def update(self, instance, validated_data):
        validated_data.pop("user", None)
        return super().update(instance, validated_data)


class ImageLikeDislikeModelSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    image = ImageModelSerializer()

    class Meta:
        model = ImageLikeDislikeModel
        fields = "__all__"


class ImageCommentModelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    image = ImageModelSerializer(read_only=True)

    class Meta:
        model = ImageCommentModel
        fields = "__all__"


    def validate(self, attrs):
        if len(attrs.get("comment")) > 400:
            raise serializers.ValidationError(
                "Comment length must be less than 501 characters."
            )
        return attrs
