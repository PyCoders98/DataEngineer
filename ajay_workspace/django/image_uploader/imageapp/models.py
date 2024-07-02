from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField( upload_to="media")
    desc = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.desc