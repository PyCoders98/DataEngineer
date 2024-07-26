from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.forms import ModelForm


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mob = models.CharField(max_length=12, default="")


class Post(models.Model):
    title = models.CharField(max_length=124, default="")


def save_post(sender, instance, **kwargs):
    print("signals")


def save_pre(sender, instance, **keargs):
    print("pre_save")


post_save.connect(save_post, sender=Post)
pre_save.connect(save_pre, sender=Post)


class Office(models.Model):
    name = models.CharField(max_length=124, default="")
    location = models.CharField(max_length=124, default="")


class Employee(models.Model):
    genders = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    first_name = models.CharField(max_length=124, default="")
    last_name = models.CharField(max_length=124, default="")
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=20, choices=genders)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)


class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = "__all__"


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
