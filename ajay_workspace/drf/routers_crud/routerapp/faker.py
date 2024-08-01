from faker import Faker
import random
from .models import *

def insert_personnel_info():
    fake = Faker()
    for i in range(500):
        name = fake.name()
        father = fake.name()
        mother = fake.name()
        age = random.randint(15,40)
        PersonnelInfo.objects.create(name=name, father=father, mother=mother, age=age)
