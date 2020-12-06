# Generated by Django 3.1.4 on 2020-12-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0041_firmaracta'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActaFirmas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesorguia', models.CharField(max_length=50)),
                ('profesorinvitado1', models.CharField(max_length=50)),
                ('profesorinvitado2', models.CharField(max_length=50)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FirmarActa',
        ),
    ]