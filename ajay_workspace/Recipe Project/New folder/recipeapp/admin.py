from django.contrib import admin
from .models import *
# Register your models here.
class ReceipeModel(admin.ModelAdmin):   
    list_display = ('receipe_name','category',)
admin.site.register(Receipe,ReceipeModel)
admin.site.register(Category)