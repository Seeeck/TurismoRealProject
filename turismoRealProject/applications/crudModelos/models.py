from django.db import models
from django.db.models.fields import AutoField
from applications.users.models import User
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

    def __str__(self):
        return "id_departamento:"+str(self.id_departamento)+" numero departamento:"+str(self.numero_departamento) 
    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
        ordering=['nombre_departamento']




""" 
class Funcionario(models.Model):
    rut_funcionario = models.CharField(max_length=50)
    nombre_funcionario = models.CharField(max_length=50)
    apellido_funcionario = models.CharField(max_length=50)
    fecha_nacimeinto = models.DateField()
    id_usuario=models.ForeignKey(User,on_delete=models.CASCADE)

class CheckIn(models.Model):
    id_checkin = models.CharField(primary_key=True, max_length=50)
    fecha_checkin = models.DateField()
    lista_checkeo = models.CharField(max_length=100)
    documento_pdf = models.FileField(upload_to=None, max_length=100)
    id_funcionario=models.ForeignKey(Funcionario,on_delete=models.CASCADE)

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

class CheckOut(models.Model):
    id_checkout = models.CharField(primary_key=True, max_length=50)
    fecha_checkout=models.DateField()



class Reserva(models.Model):
    id_reserva = models.CharField(primary_key=True,  max_length=50)
    valor_total = models.IntegerField()
    primer_pago_anticipo = models.IntegerField()
    segundo_pago_checkin = models.IntegerField()
    tercer_pago_checkout = models.IntegerField()
    is_primerPago = models.BooleanField()
    is_segundoPago = models.BooleanField()
    is_tercerPago = models.BooleanField()

 """