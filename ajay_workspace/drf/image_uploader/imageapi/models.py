from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    profile_image = models.ImageField(upload_to="media", null=True, blank=True)
    liked_images = models.ImageField(upload_to="liked_images", null=True, blank=True)
    disliked_images = models.ImageField(
        upload_to="disliked_images", null=True, blank=True
    )


class ImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    thumbnail = models.CharField(max_length=500)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(
        auto_created=True,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self) -> str:
        return self.user.username


class ImageCommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self) -> str:
        return self.image.user.username


class ImageLikeDislikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.like)
