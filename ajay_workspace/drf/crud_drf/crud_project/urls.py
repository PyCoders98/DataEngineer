from django.contrib import admin
from django.urls import path, include
import crud_app
import crudauth
from crudauth import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register("studentapi", views.StudentModelViewSet, basename="student")

urlpatterns = [
    path("gettoken/", obtain_auth_token),
    path("admin/", admin.site.urls),
    path("crud/", include("crud_app.urls")),
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
]
