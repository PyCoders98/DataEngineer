from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.category
class Receipe(models.Model):
    # user = models.ForeignKey(User,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.SET_NULL,null = True,blank = True)
    category = models.ForeignKey(Category,on_delete = models.SET_NULL,null=True,default=1)
    receipe_name=models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    receipe_ingredients = models.CharField(max_length=1000,null=True,blank=True)
    receipe_making_process = models.CharField(max_length=1500,null=True,blank=True)
    
    

    
