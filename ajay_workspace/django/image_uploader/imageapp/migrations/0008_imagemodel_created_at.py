# Generated by Django 5.0.6 on 2024-07-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imageapp", "0007_imagemodel_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagemodel",
            name="created_at",
            field=models.DateTimeField(auto_created=True, auto_now=True, null=True),
        ),
    ]
