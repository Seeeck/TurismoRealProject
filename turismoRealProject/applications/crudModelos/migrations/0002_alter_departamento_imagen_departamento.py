# Generated by Django 3.2.7 on 2021-09-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudModelos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='imagen_departamento',
            field=models.ImageField(blank=True, height_field=400, null=True, upload_to='images'),
        ),
    ]
