# Generated by Django 3.1.1 on 2020-10-31 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0028_remove_tarea_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='exigencia',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='nota',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]