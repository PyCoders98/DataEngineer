from rest_framework import serializers
from .models import *


class StudentInfoSerializer(serializers.Serializer):
    sname = serializers.CharField(max_length=40)
    fname = serializers.CharField(max_length=40)
    address = serializers.CharField(max_length=100)
    email = serializers.EmailField(
        max_length=100,
    )
    phone = serializers.IntegerField()

    def validate(self, data):
        phone = data.get('phone')
        if len(str(phone))<10:
            raise serializers.ValidationError("Phone number is must be 10 digit long.")
        return data
    def create(self, validated_data):
        data = studentInfo.objects.create(**validated_data)
        return data

    def update(self, instance, validated_data):
        instance.sname = validated_data.get("sname", instance.sname)
        instance.fname = validated_data.get("fname", instance.fname)
        instance.address = validated_data.get("address", instance.address)
        instance.email = validated_data.get("email", instance.email)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.save()
        return instance
