# Generated by Django 4.2.11 on 2024-05-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessheadquater', '0004_rename_sitemember_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
