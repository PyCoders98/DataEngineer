from rest_framework import serializers
from .models import PersonnelInfo

class PersonnelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonnelInfo
        fields = '__all__'