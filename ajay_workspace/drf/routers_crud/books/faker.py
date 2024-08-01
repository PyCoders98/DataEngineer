from faker import Faker
from .models import Author, Book
import random
def author():
    for i in range(50):
        fake = Faker()
        author = Author.objects.create(name=fake.name())

def books():
    auhtor = Author.objects.all()
    for i in range(100):
        fake = Faker()
        book = Book.objects.create(title=fake.text(max_nb_chars=100), author=random.choice(auhtor))
