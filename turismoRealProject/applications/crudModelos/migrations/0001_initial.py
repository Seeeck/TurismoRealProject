# Generated by Django 3.2.7 on 2021-10-23 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id_checkin', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_checkin', models.DateField()),
                ('lista_checkeo', models.CharField(max_length=100, null=True)),
                ('documento_pdf', models.FileField(null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id_checkout', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_checkout', models.DateField()),
                ('costo_reparacion', models.IntegerField(null=True)),
                ('valor_servicio_extra', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('imagen_departamento', models.ImageField(blank=True, null=True, upload_to='images')),
                ('nombre_departamento', models.CharField(max_length=60)),
                ('numero_departamento', models.IntegerField()),
                ('direccion_departamento', models.CharField(max_length=60, null=True)),
                ('numero_personas', models.IntegerField()),
                ('valor_dia', models.IntegerField()),
                ('valor_anticipo', models.IntegerField()),
                ('estado_departamento', models.BooleanField(default=True, verbose_name='Esta disponible')),
                ('is_tour', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('is_transporte', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True, null=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['nombre_departamento'],
            },
        ),
        migrations.CreateModel(
            name='PersonaExtra',
            fields=[
                ('id_persona_extra', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('apellido', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sv_Tour',
            fields=[
                ('id_tour', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tour', models.CharField(default='', max_length=60)),
                ('valor_tour', models.IntegerField(default=0)),
                ('fecha_registro_tour', models.DateField(null=True)),
                ('descripcion_tour', models.CharField(default='', max_length=200)),
            ],
            options={
                'verbose_name': 'Tour',
            },
        ),
        migrations.CreateModel(
            name='Sv_Transporte',
            fields=[
                ('id_sv_transporte', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_chofer', models.CharField(max_length=30, null=True)),
                ('apellido_chofer', models.CharField(max_length=30, null=True)),
                ('patente_vehiculo', models.CharField(max_length=10, null=True)),
                ('valor_transporte', models.IntegerField(default=0)),
                ('sv_transporte_disponible', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Servicio de transporte',
                'verbose_name_plural': 'Servicios de transporte',
            },
        ),
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
            name='Transporte',
            fields=[
                ('id_transporte', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ida', models.DateField(null=True)),
                ('fecha_vuelta', models.DateField(null=True)),
                ('direccion_inicio', models.CharField(max_length=50, null=True)),
                ('fecha_solicitud', models.DateField(auto_now=True)),
                ('id_sv_transporte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudModelos.sv_transporte')),
            ],
            options={
                'verbose_name': 'Transporte',
                'verbose_name_plural': 'Transportes',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('valor_total', models.IntegerField(default=0)),
                ('valor_transporte', models.IntegerField(default=0)),
                ('valor_tour', models.IntegerField(default=0)),
                ('valor_reserva_departamento', models.IntegerField(default=0)),
                ('is_pago_anticipo', models.BooleanField(default=False)),
                ('is_pago_checkin', models.BooleanField(default=False)),
                ('is_pago_checkout', models.BooleanField(default=False)),
                ('is_transporte', models.BooleanField(default=False)),
                ('is_tour', models.BooleanField(default=False)),
                ('id_check_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudModelos.checkin')),
                ('id_check_out', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudModelos.checkout')),
            ],
        ),
    ]
