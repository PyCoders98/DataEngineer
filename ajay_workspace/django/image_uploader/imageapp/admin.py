from django.contrib import admin
from imageapp.models import *
from django.contrib.auth.admin import UserAdmin


class UserDetails(admin.ModelAdmin):
    list_display = ("id", "username", "email", "profile_image")


admin.site.register(User, UserDetails)


class ImageModelDetails(admin.ModelAdmin):
    list_display = ("id", "user", "like", "dislike", "created_at")
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


class RequestDetails(admin.ModelAdmin):
    list_display = ("id", "receiver_user", "sender_user", "send_at")


admin.site.register(RequestModel, RequestDetails)


class FollowerDetails(admin.ModelAdmin):
    list_display = ("id", "user", "follower", "following")


admin.site.register(FollowerModel, FollowerDetails)
