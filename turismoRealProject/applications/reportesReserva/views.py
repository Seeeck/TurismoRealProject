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
            
            total_semanal=0
            total_tour_semanal=0
            total_transporte_semanal=0
            total_reserva_dias_departamento=0
            for reserva in reservas:
                total_semanal=total_semanal+reserva.valor_total
                total_tour_semanal=total_tour_semanal+reserva.valor_tour
                total_transporte_semanal=total_transporte_semanal+reserva.valor_transporte
                total_reserva_dias_departamento=total_reserva_dias_departamento+reserva.valor_reserva_departamento
            
            cantidad_reservas_semanal=reservas.count()

            #Semana anterior
            reservas_semana_anterior=Reserva.objects.filter(fecha_fin_reserva__week=num_semana-1)
            total_semanal_sa=0
            total_tour_semanal_sa=0
            total_transporte_semanal_sa=0
            for reserva in reservas_semana_anterior:
                total_semanal_sa=total_semanal_sa+reserva.valor_total
                total_tour_semanal_sa=total_tour_semanal_sa+reserva.valor_tour
                total_transporte_semanal_sa=total_transporte_semanal_sa+reserva.valor_transporte
            

            total_diferencia_sa=total_semanal-total_semanal_sa
            total_diferencia_tour_sa=total_tour_semanal-total_tour_semanal_sa
            total_diferencia_transporte_sa=total_transporte_semanal-total_transporte_semanal_sa


            aumento_total=""
            porcentaje_aumento_total=0
            if(total_semanal>total_semanal_sa):
                aumento_total= "+"+str(total_diferencia_sa)
                porcentaje_aumento_total=round((total_semanal_sa*100)/total_semanal,1)
            else:
                aumento_total= "-"+str(total_diferencia_sa)

            aumento_tour=""
            if(total_tour_semanal>total_tour_semanal_sa):
                aumento_tour="+"+str(total_diferencia_tour_sa)
            else:
                aumento_tour="-"+str(total_diferencia_tour_sa)
            
            aumento_transporte=""
            if(total_transporte_semanal>total_diferencia_tour_sa):
                aumento_transporte="+"+str(total_diferencia_transporte_sa)
            else:
                aumento_transporte="-"+str(total_diferencia_transporte_sa)
            #Fin semama anterior

            context={
                'reporte_week':True,
                'total_semanal':total_semanal,
                'total_tour_semanal':total_tour_semanal,
                'total_transporte_semanal':total_transporte_semanal,
                'cantidad_reservas_semanal':cantidad_reservas_semanal,
                'aumento_total':aumento_total,
                'porcentaje_aumento_total':porcentaje_aumento_total,
                'aumento_tour':aumento_tour,
                'aumento_transporte':aumento_transporte,
                'total_reserva_dias_departamento':total_reserva_dias_departamento
            }
            return render(request,'admin/reportes_template.html',context)

        
    

    