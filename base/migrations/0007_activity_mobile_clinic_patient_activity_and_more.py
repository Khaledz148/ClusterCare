# Generated by Django 4.2.4 on 2023-09-15 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_activity_crisis_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='mobile_clinic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.mobileclinic'),
        ),
        migrations.AddField(
            model_name='patient',
            name='Activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.activity'),
        ),
        migrations.AddField(
            model_name='resources',
            name='mobile_clinic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.mobileclinic'),
        ),
    ]
