# Generated by Django 3.1.4 on 2020-12-06 00:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0046_auto_20201205_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='actafirmas',
            name='Alumno',
            field=models.CharField(max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actafirmas',
            name='Rut_Alumno',
            field=models.CharField(max_length=50),
            preserve_default=False,
        ),
    ]
