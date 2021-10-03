from django.db import models
from django.db.models.fields import AutoField
from applications.users.models import User,Cliente
from turismoRealProject.settings.local import BASE_DIR

# Create your models here.
class Zona(models.Model):
    id_zona = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.comuna
    class Meta:
        verbose_name='Zona'

class Sv_Transporte(models.Model):
    id_transporte=models.AutoField(primary_key=True)
    nombre_chofer=models.CharField(max_length=30,null=True)
    apellido_chofer=models.CharField(max_length=30,null=True)
    patente_vehiculo=models.CharField(max_length=10,null=True)
    fecha_ida=models.DateField(null=True)
    fecha_vuelta=models.DateField(null=True)
    direccion_inicio=models.CharField(max_length=50,null=True)
    valor_transporte=models.IntegerField(default=0)
    fecha_solicitud=models.DateField(auto_now=True)

class Sv_Tour(models.Model):
    id_tour=models.AutoField(primary_key=True)
    valor_tour=models.IntegerField(default=0)
    fecha_registro_tour=models.DateField(null=True)
    descripcion_tour=models.CharField(max_length=200,default='')

class Departamento(models.Model):
    ESTADOS_DEPARTAMENTO=(
        ('O','Ocupado'),
        ('D','Disponible')
    )
    id_departamento = models.AutoField(primary_key=True)
    imagen_departamento=models.ImageField(upload_to='images',blank=True, null=True)
    nombre_departamento = models.CharField(max_length=60)
    numero_departamento = models.IntegerField()
    numero_personas= models.IntegerField()
    valor_dia = models.IntegerField()
    valor_anticipo = models.IntegerField()
    estado_departamento = models.CharField(choices=ESTADOS_DEPARTAMENTO,max_length=1)
    id_zona = models.ForeignKey(Zona,on_delete=models.CASCADE)
    id_tour=models.ForeignKey(Sv_Transporte,on_delete=models.CASCADE,null=True)
    id_transporte=models.ForeignKey(Sv_Tour,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "id_departamento:"+str(self.id_departamento)+" numero departamento:"+str(self.numero_departamento) 
    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
        ordering=['nombre_departamento']

class CheckIn(models.Model):
    id_checkin = models.CharField(primary_key=True, max_length=50)
    fecha_checkin = models.DateField()
    lista_checkeo = models.CharField(max_length=100,null=True)
    documento_pdf = models.FileField(upload_to=None, max_length=100,null=True)

class CheckOut(models.Model):
    id_checkout = models.CharField(primary_key=True, max_length=50)
    fecha_checkout=models.DateField()
    costo_reparacion=models.IntegerField(null=True)
    valor_servicio_extra=models.IntegerField(null=True)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    valor_total = models.IntegerField(default=0)
    is_pago_anticipo = models.BooleanField(default=False)
    is_pago_checkin = models.BooleanField(default=False)
    is_pago_checkout = models.BooleanField(default=False)
    id_departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE,null=True)
    id_cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
    id_check_in=models.ForeignKey(CheckIn,on_delete=models.CASCADE,null=True)
    id_check_out=models.ForeignKey(CheckOut,on_delete=models.CASCADE,null=True)


class PersonaExtra(models.Model):
    rut=models.CharField(primary_key=True,max_length=30)
    nombre=models.CharField(max_length=30,null=True)
    apellido=models.CharField(max_length=30,null=True)
    id_reserva=models.ForeignKey(Reserva,on_delete=models.CASCADE,null=True)

"""



class Prop_inventario(models.Model):
    cod_prop_inventario = models.CharField(primary_key=True, max_length=50)
    nombre_propiedad = models.CharField(max_length=50)
    valor = models.IntegerField()
    fecha_registro = models.DateField(auto_now=True)
    descripcion_propiedad = models.CharField(max_length=200)
    estado_propiedad_invt=models.CharField(max_length=1)
    checkins=models.ManyToManyField(CheckIn)
    id_departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE)

    def __str__(self):
        return "codigo de propiedad:"+self.cod_prop_inventario+" nombre propiedad:"+self.nombre_propiedad
    class Meta:
        verbose_name='Prop_iventario'


 """