from django.shortcuts import render
from applications.crudModelos.models import Reserva
# Create your views here.


def reportesView(request):

    if(request.method=='GET'):
        return render(request,'admin/reportes_template.html')

    if(request.method=='POST'):
        if(len(request.POST.get('week'))>0):
            semana=request.POST.get('week')
            num_semana=int(semana.split("W",1)[1]) 
            reservas=Reserva.objects.filter(fecha_fin_reserva__week=num_semana)
            
            total=0
            for reserva in reservas:
                total=total+reserva.valor_total
            total_semanañ=total
            cantidad_reservas_semanal=reservas.count()
            """ total_tour_semanal=
            total_transporte_semanal=
            total_diferencia_semana_anterior=
            porcentaje_semana_anterior=
            total_diferencia_semana_posterior=
            porcentaje_semana_posterior= """
            print(reservas.count())

            return render(request,'admin/reportes_template.html')

        
    

    