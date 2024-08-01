from django.urls import path
from crud_app import views
from .views import StudentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path("crudrt/", views.StudentAPI.as_view()),
    path("generic-student/", views.StudentGenerics.as_view()),
    path("generic-student/<id>", views.StudentGenericsUpdateDelete.as_view()),
    path('', include(router.urls)),
]
