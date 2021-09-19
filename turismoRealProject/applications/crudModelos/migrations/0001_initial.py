# Generated by Django 3.2.7 on 2021-09-19 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id_zona', models.AutoField(primary_key=True, serialize=False)),
                ('comuna', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Zona',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('imagen_departamento', models.ImageField(blank=True, null=True, upload_to='images')),
                ('nombre_departamento', models.CharField(max_length=60)),
                ('numero_departamento', models.IntegerField()),
                ('numero_personas', models.IntegerField()),
                ('valor_dia', models.IntegerField()),
                ('valor_anticipo', models.IntegerField()),
                ('estado_departamento', models.CharField(choices=[('O', 'Ocupado'), ('D', 'Disponible')], max_length=1)),
                ('id_zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudModelos.zona')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['nombre_departamento'],
            },
        ),
    ]
