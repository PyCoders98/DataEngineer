from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *


class StudentAPI(APIView):

    def post(self, request, format=None):
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, format=None):
        if id is None:
            students = studentInfo.objects.all()
            serializer = StudentInfoSerializer(students, many=True)
            return Response(serializer.data)
        else:
            try:
                stu = studentInfo.objects.get(id=id)
                serializer = StudentInfoSerializer(stu)
                return Response(serializer.data)
            except:
                return Response(
                    {"msg": "No Data Found"}, status=status.HTTP_404_NOT_FOUND
                )

    def put(self, request, id, format=None):
        try:
            student = studentInfo.objects.get(id=id)
            serializer = StudentInfoSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Data Updated"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"msg": "Data Does Not Exist!"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id, format=None):
        try:
            student = studentInfo.objects.get(id=id)
            student.delete()
            return Response({"msg": "Successfully Deleted."}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"msg": "Data Does Not Exist!"}, status=status.HTTP_400_BAD_REQUEST
            )
