from django.db import models

# Create your models here.
class FormModel(models.model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name
    