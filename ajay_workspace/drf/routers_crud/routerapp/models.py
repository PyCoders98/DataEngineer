from django.db import models


# Create your models here.
class PersonnelInfo(models.Model):
    name = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    mother = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name},{self.father}, {self.mother}, {self.age}"
