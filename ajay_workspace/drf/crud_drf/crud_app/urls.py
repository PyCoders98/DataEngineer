from django.urls import path
from crud_app import views

urlpatterns = [
    path("add/", views.StudentAPI.as_view()),
    path("get/<int:id>", views.StudentAPI.as_view()),
    path("get/", views.StudentAPI.as_view()),
    path("update/<int:id>", views.StudentAPI.as_view()),
    path("delete/<int:id>", views.StudentAPI.as_view()),
]
