# Generated by Django 3.0.7 on 2020-07-19 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0011_auto_20200719_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='archivo',
            new_name='documento',
        ),
    ]
