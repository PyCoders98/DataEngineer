from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PersonnelInfoViewSet

router = SimpleRouter()
router.register(r"personnelinfo", PersonnelInfoViewSet,basename="u")

urlpatterns = [
    path("", include(router.urls)),
]
