# Generated by Django 5.0.6 on 2024-07-22 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("imageapi", "0002_rename_imagecomment_imagecommentmodel"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ImageLikeDislike",
            new_name="ImageLikeDislikeModel",
        ),
    ]
