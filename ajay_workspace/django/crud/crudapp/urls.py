from django.urls import path
from .views import AboutPageView, ListPageView

urlpatterns = [
    path("<int:pk>", AboutPageView.as_view(), name="about-page"),
    path("", AboutPageView.as_view(), name="about-page"),
    path("list-view/", ListPageView.as_view()),
]
