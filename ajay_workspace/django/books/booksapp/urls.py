from django.urls import path
from .views import *

urlpatterns = [
    path("crud/", home, name="home_page"),
    path("text/",text),
]
