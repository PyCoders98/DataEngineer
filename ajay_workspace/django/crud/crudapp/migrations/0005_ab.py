# Generated by Django 5.0.6 on 2024-08-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crudapp", "0004_office_employee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ab",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=124)),
                ("name2", models.CharField(default="", max_length=124)),
                ("name3", models.CharField(default="", max_length=124)),
            ],
        ),
    ]
