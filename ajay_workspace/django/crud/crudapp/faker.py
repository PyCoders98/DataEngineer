from .models import Ba, Bacd, Bac
from faker import Faker


def insert():
    fake = Faker()
    for i in range(100):
        name1 = fake.name()
        name2 = fake.name()
        name3 = fake.name()
        name5 = fake.name()
        Bacd.objects.create(name=name1, name2=name2, name3=name3, name5=name5)

def insert2():
    fake = Faker()
    obj = Bac.objects.all()
    for i in obj:
        name6=fake.name()
        Bacd.objects.create(name6 = fake.name())
