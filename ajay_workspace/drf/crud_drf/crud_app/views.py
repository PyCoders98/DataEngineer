from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from rest_framework import generics


class StudentGenerics(
    generics.ListAPIView, generics.CreateAPIView, generics.ListCreateAPIView
):
    queryset = studentInfo.objects.all()
    serializer_class = StudentInfoSerializer


class StudentGenericsUpdateDelete(
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.RetrieveAPIView,
):
    queryset = studentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    lookup_field = "id"


class StudentAPI(APIView):
    def post(self, request, format=None):
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            data = JSONParser().parse(stream)
            serializer = StudentInfoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):

        id = request.data.get("id")
        # id = data.get('id')
        if id is None:
            students = studentInfo.objects.all()
            serializer = StudentInfoSerializer(students, many=True)
            print(serializer)
            json_data = JSONRenderer().render(serializer.data)
            print(type(json_data))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                stu = studentInfo.objects.get(id=id)
                serializer = StudentInfoSerializer(stu)
                return Response(serializer.data, status=status.HTTP_302_FOUND)
            except:
                return Response(
                    {"msg": "No Data Found"}, status=status.HTTP_404_NOT_FOUND
                )

    def put(self, request, id=None, format=None):
        id = request.data.get("id")
        try:
            student = studentInfo.objects.get(id=id)
            serializer = StudentInfoSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Data Updated"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
        except:
            return Response(
                {"msg": "Data Does Not Exist!"}, status=status.HTTP_304_NOT_MODIFIED
            )

    def patch(self, request, id=None, format=None):
        id = request.data.get("id")
        try:
            student = studentInfo.objects.get(id=id)
            serializer = StudentInfoSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Data Updated"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"msg": "Data Does Not Exist!"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id=None, format=None):
        id = request.data.get("id")
        try:
            student = studentInfo.objects.get(id=id)
            student.delete()
            return Response({"msg": "Successfully Deleted."}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"msg": "Data Does Not Exist!"}, status=status.HTTP_400_BAD_REQUEST
            )
