from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("office/", office_crud, name="office_crud"),
    path("employee/", employee_crud, name="employee_crud"),
    path("offices/", get_all_offices, name="get_all_offices"),
    path("employees/", get_all_employees, name="get_all_employees"),
]
