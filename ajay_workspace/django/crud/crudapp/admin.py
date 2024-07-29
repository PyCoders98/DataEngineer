from django.contrib import admin
from .models import *

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'office')

# Register your models here.
admin.site.register(Office)
admin.site.register(Employee, EmployeeAdmin)