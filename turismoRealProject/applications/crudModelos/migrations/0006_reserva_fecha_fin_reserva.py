# Generated by Django 3.2.7 on 2021-11-08 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudModelos', '0005_auto_20211104_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fecha_fin_reserva',
            field=models.DateField(null=True),
        ),
    ]
