from django.urls import reverse
from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self) -> str:
        return f"{self.title}, {self.author.name}"


class Details(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
