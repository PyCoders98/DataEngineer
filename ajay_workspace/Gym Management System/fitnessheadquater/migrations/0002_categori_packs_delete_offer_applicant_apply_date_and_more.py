# Generated by Django 4.2.11 on 2024-05-07 09:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessheadquater', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Packs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('price', models.IntegerField()),
                ('regular_price', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fitnessheadquater.categori')),
            ],
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.AddField(
            model_name='applicant',
            name='apply_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='buy_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fitnessheadquater.packs'),
        ),
    ]
