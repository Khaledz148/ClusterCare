# Generated by Django 4.2.4 on 2023-09-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobileclinic',
            name='clinic_services',
            field=models.CharField(choices=[('H', 'Helth'), ('E', 'Education')], max_length=1, null=True),
        ),
    ]
