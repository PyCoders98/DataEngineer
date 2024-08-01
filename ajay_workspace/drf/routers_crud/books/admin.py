from django.contrib import admin

# Register your models here.
from .models import Book, Author

class Books(admin.ModelAdmin):
    list_display = ["title","author"]

admin.site.register(Book,Books)

class Authors(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Author,Authors)
    

