from django.urls import path
from .views import *

urlpatterns = [
    path("crud/", home, name="home_page"),
    path("text/", text),
    path("details/<int:pk>/", article_detail, name="article_detail"),
]
