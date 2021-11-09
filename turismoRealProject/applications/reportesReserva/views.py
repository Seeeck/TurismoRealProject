from django.shortcuts import render
from applications.crudModelos.models import Reserva
import datetime
# Create your views here.


def reportesView(request):

    if(request.method=='GET'):
        context={
            'is_reporte':False
        }
        return render(request,'admin/reportes_template.html',context)

    if(request.method=='POST'):
        if(request.POST.get('week')):
            semana=request.POST.get('week')
            num_semana=int(semana.split("W",1)[1]) 
            reservas=Reserva.objects.filter(fecha_fin_reserva__week=num_semana)
            inicio_semana = datetime.datetime.strptime(semana+ '-1', "%Y-W%W-%w").strftime("%d/%m/%y")
            fin_semana=datetime.datetime.strptime(semana+ '-0', "%Y-W%W-%w").strftime("%d/%m/%y")

            is_reporte=True
            reporte_week=True
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
            is_aumento_total=False
            is_aumento_total_porcentaje =False
            if(total_diferencia_sa>=0):
                is_aumento_total=True
                is_aumento_total_porcentaje=True
                aumento_total= "+$"+str(total_diferencia_sa)
                porcentaje_aumento_total=str(   round(-1*(((total_semanal_sa*100)/total_semanal)-100),2)   )  +"%"
            else:
                is_aumento_total=False
                is_aumento_total_porcentaje=False
                aumento_total= "$"+str(total_diferencia_sa)
                porcentaje_aumento_total= str(-round((round((total_semanal_sa*100)/total_semanal,2))-100,2)  )+"%"

            aumento_tour=""
            is_aumento_total_tour=False
            if(total_diferencia_tour_sa>=0):
                is_aumento_total_tour=True
                aumento_tour="+$"+str(total_diferencia_tour_sa)
            else:
                is_aumento_total_tour=False
                aumento_tour=total_diferencia_tour_sa
            
            aumento_transporte=""
            is_aumento_total_transporte=False
            if(total_diferencia_transporte_sa>=0):
                is_aumento_total_transporte=True
                aumento_transporte="+$"+str(total_diferencia_transporte_sa)
            else:
                is_aumento_total_transporte=False
                aumento_transporte=total_diferencia_transporte_sa
            #Fin semama anterior

            context={
                'total_semanal':total_semanal,
                'total_tour_semanal':"$"+str(total_tour_semanal),
                'total_transporte_semanal':"$"+str(total_transporte_semanal),
                'cantidad_reservas_semanal':cantidad_reservas_semanal,
                'aumento_total':aumento_total,
                'porcentaje_aumento_total':porcentaje_aumento_total,
                'aumento_tour':aumento_tour,
                'aumento_transporte':aumento_transporte,
                'total_reserva_dias_departamento': "$"+str(total_reserva_dias_departamento),
                'is_aumento_total':is_aumento_total,
                'is_aumento_total_porcentaje':is_aumento_total_porcentaje,
                'is_aumento_total_tour':is_aumento_total_tour,
                'is_aumento_total_transporte':is_aumento_total_transporte,
                'inicio_semana':inicio_semana,
                'fin_semana':fin_semana,
                'is_reporte':is_reporte,
                'reporte_week':reporte_week
            }
            return render(request,'admin/reportes_template.html',context)

        if(request.POST.get('day')):
            reservas=Reserva.objects.filter(fecha_fin_reserva=request.POST.get('day'))

            is_reporte=True
            reporte_day=True
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




            return render(request,'admin/reportes_template.html')


            
    #    if(True==False):
    #            mensaje="No existen reservas"
    #            context={
    #                'mensaje':mensaje,
    #                'sin_reservas':True
    #            }
    #            return render(request,'admin/reportes_template.html',context)
        

        
    

    