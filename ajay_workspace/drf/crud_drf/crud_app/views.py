from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from .models import studentInfo
from .serializers import StudentInfoSerializer
import io
from rest_framework.viewsets import ViewSet

class StudentGenerics(generics.ListCreateAPIView):
    queryset = studentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class StudentGenericsUpdateDelete(
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.RetrieveAPIView,
):
    queryset = studentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    lookup_field = "id"
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class StudentAPI(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = StudentInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        id = request.data.get("id")
        if id is None:
            students = studentInfo.objects.all()
            serializer = StudentInfoSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                student = studentInfo.objects.get(id=id)
                serializer = StudentInfoSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except studentInfo.DoesNotExist:
                return Response({"msg": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id=None, format=None):
        id = request.data.get("id")
        try:
            student = studentInfo.objects.get(id=id)
            serializer = StudentInfoSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Data Updated"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except studentInfo.DoesNotExist:
            return Response({"msg": "Data Does Not Exist!"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id=None, format=None):
        id = request.data.get("id")
        try:
            student = studentInfo.objects.get(id=id)
            serializer = StudentInfoSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Data Updated"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except studentInfo.DoesNotExist:
            return Response({"msg": "Data Does Not Exist!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id=None, format=None):
        id = request.data.get("id")
        try:
            student = studentInfo.objects.get(id=id)
            student.delete()
            return Response({"msg": "Successfully Deleted."}, status=status.HTTP_200_OK)
        except studentInfo.DoesNotExist:
            return Response({"msg": "Data Does Not Exist!"}, status=status.HTTP_404_NOT_FOUND)


class StudentViewSet(ViewSet):

    def list(self, request):
        queryset = studentInfo.objects.all()
        serializer = StudentInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            student = studentInfo.objects.get(pk=pk)
            serializer = StudentInfoSerializer(student)
            return Response(serializer.data)
        except studentInfo.DoesNotExist:
            return Response({"msg": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            student = studentInfo.objects.get(pk=pk)
            serializer = StudentInfoSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except studentInfo.DoesNotExist:
            return Response({"msg": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            student = studentInfo.objects.get(pk=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except studentInfo.DoesNotExist:
            return Response({"msg": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def by_city(self, request):
        city = request.query_params.get('city', None)
        if city is not None:
            students = studentInfo.objects.filter(city=city)
            serializer = StudentInfoSerializer(students, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "City parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
