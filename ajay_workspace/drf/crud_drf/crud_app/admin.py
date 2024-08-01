from django.contrib import admin

# Register your models here.

from .models import *


class StudentDetails(admin.ModelAdmin):
    list_display = ["id", "sname", "fname", "email", "phone", "city"]


admin.site.register(studentInfo, StudentDetails)
