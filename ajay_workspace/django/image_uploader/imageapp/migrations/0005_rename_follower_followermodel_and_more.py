# Generated by Django 5.0.7 on 2024-08-05 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("imageapp", "0004_follower_request"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Follower",
            new_name="FollowerModel",
        ),
        migrations.RenameModel(
            old_name="Request",
            new_name="RequestModel",
        ),
    ]
