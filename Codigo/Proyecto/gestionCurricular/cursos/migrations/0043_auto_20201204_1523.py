# Generated by Django 3.1.4 on 2020-12-04 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0042_auto_20201204_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actafirmas',
            old_name='profesorguia',
            new_name='Profesor_guia',
        ),
        migrations.RenameField(
            model_name='actafirmas',
            old_name='profesorinvitado1',
            new_name='Profesor_invitado_1',
        ),
        migrations.RenameField(
            model_name='actafirmas',
            old_name='profesorinvitado2',
            new_name='Profesor_invitado_2',
        ),
    ]
