from django.contrib import admin
from imageapp.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserDetails(admin.ModelAdmin):
    list_display = ("username", "email", "password", "profile_image")


# admin.site.unregister(User)
# admin.site.register(User, UserDetails)


class ImageModelDetails(admin.ModelAdmin):
    list_display = ("user", "like", "dislike", "created_at")
    prepopulated_fields = {
        "slug": ("user", "like", "dislike")
    }  # Use '__' to access related fields

    def save_model(self, request, obj, form, change):
        """Override save_model to set slug based on username."""
        if not obj.slug:  # Only set slug if it's not already set
            obj.slug = obj.user.username
        super().save_model(request, obj, form, change)


admin.site.register(ImageModel, ImageModelDetails)
admin.site.register(ImageComment)
admin.site.register(ImageLike)
