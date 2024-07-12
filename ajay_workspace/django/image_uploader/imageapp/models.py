from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pofile_image = models.ImageField(upload_to="profile_image", null=True)
    image = models.ImageField(upload_to="media")
    desc = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_created=True, auto_now=True, null=True)

    def __str__(self) -> str:
        return self.user.username


class ImageComment(models.Model):
    username = models.CharField(max_length=300, default="h")
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self) -> str:
        return self.image.user.username


class ImageLike(models.Model):
    username = models.CharField(max_length=300, default="h")
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.like)
