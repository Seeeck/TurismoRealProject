import schedule
import time
import datetime
from applications.crudModelos.models import CheckOut

def generarReporteSemanal():
    if_checkout=CheckOut.objects.create(fecha_checkout=datetime.date.today(),costo_reparacion=123456789)
    print(if_checkout)

schedule.every(5).seconds.do(generarReporteSemanal)


while True:
    schedule.run_pending()
    time.sleep(1)

class CheckOut(models.Model):
    id_checkout = models.AutoField(primary_key=True)
    fecha_checkout=models.DateField()
    costo_reparacion=models.IntegerField(null=True)
    valor_servicio_extra=models.IntegerField(null=True)