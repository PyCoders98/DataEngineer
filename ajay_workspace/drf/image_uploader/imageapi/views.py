from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class RegisterUser(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):

    #     serializer = UserSerializer(data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.data.get("id") == None:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                data = User.objects.get(id=request.data.get("id"))
                serializer = UserSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)


class AuthenticateView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(
                {"error": "Username and password are required!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST
        )


class ImageModelView(APIView):
    def post(self, request):
        serializer = ImageModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.data.get("id") == None:
            data = ImageModel.objects.all()
            serializer = ImageModelSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                data = ImageModel.objects.get(id=request.data.get("id"))
                serializer = ImageModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            model_instance = ImageModel.objects.get(id=request.data.get("id"))
            serializer = ImageModelSerializer(
                model_instance, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            model_instance = ImageModel.objects.get(id=request.data.get("id"))
            model_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ImageCommentModelView(APIView):
    def post(self, request):
        serializer = ImageCommentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.data.get("id") is None:
            data = ImageCommentModel.objects.all()
            serializer = ImageCommentModelSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                data = ImageCommentModel.objects.get(id=request.data.get("id"))
                serializer = ImageCommentModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            model_instance = ImageCommentModel.objects.get(id=request.data.get("id"))
            serializer = ImageCommentModelSerializer(model_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        try:
            model_instance = ImageCommentModel.objects.get(id=request.data.get("id"))
            serializer = ImageCommentModelSerializer(
                model_instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ImageLikeDislikeModelView(APIView):
    def post(self, request):
        serializer = ImageLikeDislikeModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.data.get("id") is None:
            print("inside")
            data = ImageLikeDislikeModel.objects.all()
            serializer = ImageLikeDislikeModelSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                data = ImageLikeDislikeModel.objects.get(id=request.data.get("id"))
                serializer = ImageLikeDislikeModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            model_instance = ImageLikeDislikeModel.objects.get(
                id=request.data.get("id")
            )
            serializer = ImageLikeDislikeModelSerializer(
                model_instance, data=request.data
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        try:
            model_instance = ImageLikeDislikeModel.objects.get(
                id=request.data.get("id")
            )
            serializer = ImageLikeDislikeModelSerializer(
                model_instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
