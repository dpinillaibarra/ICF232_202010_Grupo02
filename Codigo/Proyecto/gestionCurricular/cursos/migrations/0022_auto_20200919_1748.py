# Generated by Django 3.1.1 on 2020-09-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0021_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descripcion',
            name='descripcion',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
