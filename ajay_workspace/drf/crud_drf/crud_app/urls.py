from django.urls import path
from crud_app import views

urlpatterns = [
    path("crud/", views.StudentAPI.as_view()),
    path("generic-student/", views.StudentGenerics.as_view()),
    path("generic-student/<id>", views.StudentGenericsUpdateDelete.as_view()),
]
