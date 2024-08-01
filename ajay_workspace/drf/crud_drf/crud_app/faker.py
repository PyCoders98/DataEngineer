from faker import Faker
from .models import studentInfo


def generate_students():
    for i in range(500):
        fake = Faker()
        sname = fake.name()
        fname = fake.name()
        address = fake.address()
        email = fake.email()
        phone = fake.phone_number()

        studentInfo.objects.create(
            sname=sname, fname=fname, address=address, email=email, phone=phone
        )


def insert_city():
    sudent = studentInfo.objects.all()
    for student in sudent:
        fake = Faker()
        student.city = fake.city()
        student.save()
        