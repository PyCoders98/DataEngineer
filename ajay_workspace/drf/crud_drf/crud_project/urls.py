from django.contrib import admin
from django.urls import path, include
import crud_app

urlpatterns = [path("admin/", admin.site.urls), path("", include("crud_app.urls"))]
