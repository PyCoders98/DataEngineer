# Generated by Django 5.0.6 on 2024-07-16 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("imageapp", "0016_alter_imagemodel_pofile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="imagemodel",
            name="pofile_image",
        ),
        migrations.DeleteModel(
            name="ProfileImage",
        ),
    ]
