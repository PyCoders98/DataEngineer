from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("office/",office_crud,name="office_crud"),

]
