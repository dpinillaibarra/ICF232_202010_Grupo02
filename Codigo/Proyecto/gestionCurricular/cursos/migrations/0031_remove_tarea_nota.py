# Generated by Django 3.1.1 on 2020-10-31 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0030_remove_tarea_upload_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='nota',
        ),
    ]
