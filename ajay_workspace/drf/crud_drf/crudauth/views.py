from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes =[BasicAuthentication]
    # authentication_classes = [SessionAuthentication]

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
