# Generated by Django 3.2.7 on 2021-10-07 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crudModelos', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='id_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.cliente'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='id_departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudModelos.departamento'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='id_transporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudModelos.transporte'),
        ),
        migrations.AddField(
            model_name='personaextra',
            name='id_reserva',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudModelos.reserva'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='id_sv_transporte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudModelos.sv_transporte'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='id_tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudModelos.sv_tour'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='id_zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudModelos.zona'),
        ),
    ]