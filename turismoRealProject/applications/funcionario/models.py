from django.db import models
from applications.users.models import User
from applications.crudModelos.models import Departamento
class Funcionario(models.Model):
    
    nombre=models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    user_cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return " nombre:"+self.nombre+" "+self.apellido
    class Meta:
        verbose_name='Funcionario'




class Item(models.Model):
    ESTADO_CHOICES = [
    ('do', 'Daniado'),
    ('so', 'Sin observaciones'),
  
    ]
    nombre=models.CharField(max_length=40)
    descripcion =  models.TextField(max_length=200)
    estado= models.CharField(max_length=20,choices=ESTADO_CHOICES , default='so')
    id_departamento= models.ForeignKey(Departamento,on_delete=models.CASCADE)
    precio_estimado= models.PositiveIntegerField()
    fecha_registro= models.DateField(auto_now_add=True)

    def __str__(self):
        return "Nombre {}, Ubicado en departamento {}".format(self.nombre,self.id_departamento.numero_departamento) 


    

