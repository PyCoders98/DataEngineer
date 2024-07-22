from django.contrib import admin
from imageapi.models import *

# from django.contrib.auth.admin import UserAdmin


class UserDetails(admin.ModelAdmin):
    list_display = ("username", "email", "password", "profile_image")


class ImageModelDetails(admin.ModelAdmin):
    list_display = ("user", "likes_count", "dislikes_count", "created_at")


class ImageLikeDislikeDeatails(admin.ModelAdmin):
    list_display = ("user", "image", "like", "dislike")


admin.site.register(User, UserDetails)
admin.site.register(ImageModel, ImageModelDetails)
admin.site.register(ImageCommentModel)
admin.site.register(ImageLikeDislikeModel)
