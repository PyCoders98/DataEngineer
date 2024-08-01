from django.db import models


# Create your models here.
class studentInfo(models.Model):
    sname = models.CharField(max_length=40)
    fname = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.sname
