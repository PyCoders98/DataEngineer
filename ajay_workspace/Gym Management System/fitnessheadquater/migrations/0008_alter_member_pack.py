# Generated by Django 4.2.11 on 2024-05-10 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessheadquater', '0007_packs_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fitnessheadquater.packs'),
        ),
    ]
