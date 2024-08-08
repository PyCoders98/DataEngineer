from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.


class User(AbstractUser):
    profile_image = models.ImageField(upload_to="media", null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Unique related_name
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name=("groups"),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permission_set",  # Unique related_name
        blank=True,
        help_text=("Specific permissions for this user."),
        verbose_name=("user permissions"),
    )


class ImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Uploded By")
    image = models.ImageField(upload_to="media")
    desc = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(
        auto_created=True,
        auto_now_add=True,
    )
    slug = models.SlugField(default="", null=False)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = "Uploaded Images"
        db_table = "Uploaded Images"


class ImageComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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


class RequestModel(models.Model):
    receiver_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reciever"
    )
    sender_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sender"
    )
    send_at = models.DateTimeField(auto_now=True)


class FollowerModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post_admin",
        verbose_name="post_admin",
    )
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="follower"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="follwing"
    )
