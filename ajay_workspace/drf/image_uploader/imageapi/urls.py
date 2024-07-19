from django.urls import path
from .views import RegisterUser, AuthenticateView, ImageModelView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("register/", RegisterUser.as_view()),
    path("login/", AuthenticateView.as_view()),
    path("get-image/", ImageModelView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
