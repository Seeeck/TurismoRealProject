# Generated by Django 3.2.7 on 2021-10-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudModelos', '0004_alter_reserva_id_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='id_reserva',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]