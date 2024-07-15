from django.db import models


# Create your models here.
class FormModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name},{self.email},{self.message}"


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline


class Author(models.Model):
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.author


class Id(models.Model):
    book_id = models.IntegerField(unique=True)


class Book(models.Model):
    book_id = models.OneToOneField(Id, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name="book", on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    