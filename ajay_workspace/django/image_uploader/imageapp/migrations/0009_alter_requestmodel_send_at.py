# Generated by Django 5.0.7 on 2024-08-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imageapp", "0008_alter_followermodel_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requestmodel",
            name="send_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
