# Generated by Django 3.0.7 on 2020-07-19 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0012_auto_20200719_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='comentario',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
