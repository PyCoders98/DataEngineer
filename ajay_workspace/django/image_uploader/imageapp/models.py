from typing import Iterable
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to="media")
    desc = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment  =models.CharField(max_length=500,null=True)
    
    def __str__(self) -> str:
        return self.desc
        
