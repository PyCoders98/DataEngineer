from django.db import models
from django.contrib.auth.models import User
import math

USE_TZ = True


class SiteMember(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Registered Members"
        verbose_name_plural = "Registered Members"


class Applicant(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    file = models.FileField(upload_to="documents/")
    apply_date = models.DateTimeField(auto_now_add=True)


class Categori(models.Model):
    category = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.category
    

    class Meta:
        verbose_name = "Categories for packs"
        verbose_name_plural = "Categories for packs"



class Packs(models.Model):
    category = models.ForeignKey(Categori, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()
    regular_price = models.IntegerField()
    discount = models.IntegerField(blank=True,null=True)

    


    def __str__(self) -> str:
        return self.title


class Member(models.Model):
    user = models.ForeignKey(SiteMember, on_delete=models.CASCADE)
    pack_duraton = models.IntegerField(null=True) 
    pack_title=models.CharField(max_length=50,blank=True,null=True)
    pack_price = models.IntegerField(null=True)
    buy_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    weight = models.IntegerField(blank=True,null=True)
    end_date = models.DateTimeField()
    member = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.user.username
    
    class Meta:
        verbose_name = "People who bought packs"
        verbose_name_plural = "People who bought packs"


class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    comment = models.CharField(max_length=500, blank=False)
    date = models.DateField(auto_now_add=True)


class Owner(models.Model):
    name = "Admin"
    email = "rexempire423@gmail.com"
    password = "rexempire423"
    
    
