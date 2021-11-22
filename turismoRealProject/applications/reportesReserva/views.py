from django.shortcuts import render
from applications.crudModelos.models import Reserva
import datetime
# Create your views here.
import locale
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))

def reportesView(request):

    if(request.method=='GET'):
        context={
            'is_reporte':False
        }
        return render(request,'admin/reportes_template.html',context)
#####Week
    if(request.method=='POST'):
        if(request.POST.get('week')):
            semana=request.POST.get('week')
            num_semana=int(semana.split("W",1)[1]) 
            reservas=Reserva.objects.filter(fecha_fin_reserva__week=num_semana)

            if(reservas.count()==0):
                mensaje="No existen reservas"
                context={
                'mensaje':mensaje,
                'sin_reservas':True
                }
                return render(request,'admin/reportes_template.html',context)  

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
                porcentaje_aumento_total=str(round(-1*(((total_semanal_sa*100)/total_semanal)-100),2)   )  +"%"
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
######Day
        if(request.POST.get('day')):
            reservas=Reserva.objects.filter(fecha_fin_reserva=request.POST.get('day'))
            if(reservas.count()==0):
                mensaje="No existen reservas"
                context={
                'mensaje':mensaje,
                'sin_reservas':True
                }
                return render(request,'admin/reportes_template.html',context)  
            print(request.POST.get('day'))
            dia= datetime.datetime.strptime(request.POST.get('day'), "%Y-%m-%d").strftime("%d/%m/%y")
            is_reporte=True
            reporte_day=True
            total_dia=0
            total_tour_dia=0
            total_transporte_dia=0
            total_reserva_dias_departamento=0
            for reserva in reservas:
                total_dia=total_dia+reserva.valor_total
                total_tour_dia=total_tour_dia+reserva.valor_tour
                total_transporte_dia=total_transporte_dia+reserva.valor_transporte
                total_reserva_dias_departamento=total_reserva_dias_departamento+reserva.valor_reserva_departamento
            
            cantidad_reservas_dia=reservas.count()

            
            #Semana anterior
            
            dia_anterior=datetime.datetime.strptime(request.POST.get('day'), "%Y-%m-%d")-datetime.timedelta(days=1)
            reservas_dia_anterior=Reserva.objects.filter(fecha_fin_reserva=dia_anterior)
            print(reservas_dia_anterior)
            total_dia_da=0
            total_tour_dia_da=0
            total_transporte_dia_da=0
            for reserva in reservas_dia_anterior:
                total_dia_da=total_dia_da+reserva.valor_total
                total_tour_dia_da=total_tour_dia_da+reserva.valor_tour
                total_transporte_dia_da=total_transporte_dia_da+reserva.valor_transporte
            

            total_diferencia_da=total_dia-total_dia_da
            total_diferencia_tour_da=total_tour_dia-total_tour_dia_da
            total_diferencia_transporte_da=total_transporte_dia-total_transporte_dia_da


            aumento_total=""
            porcentaje_aumento_total=0
            is_aumento_total=False
            is_aumento_total_porcentaje =False
            if(total_diferencia_da>=0):
                is_aumento_total=True
                is_aumento_total_porcentaje=True
                aumento_total= "+$"+str(total_diferencia_da)
                porcentaje_aumento_total=str(   round(-1*(((total_dia_da*100)/total_dia)-100),2)   )  +"%"
            else:
                is_aumento_total=False
                is_aumento_total_porcentaje=False
                aumento_total= "$"+str(total_diferencia_da)
                porcentaje_aumento_total= str(-round((round((total_dia_da*100)/total_dia,2))-100,2)  )+"%"

            aumento_tour=""
            is_aumento_total_tour=False
            if(total_diferencia_tour_da>=0):
                is_aumento_total_tour=True
                aumento_tour="+$"+str(total_diferencia_tour_da)
            else:
                is_aumento_total_tour=False
                aumento_tour=total_diferencia_tour_da
            
            aumento_transporte=""
            is_aumento_total_transporte=False
            if(total_diferencia_transporte_da>=0):
                is_aumento_total_transporte=True
                aumento_transporte="+$"+str(total_diferencia_transporte_da)
            else:
                is_aumento_total_transporte=False
                aumento_transporte=total_diferencia_transporte_da
            #Fin semama anterior


            context={
                'total_dia':total_dia,
                'total_tour_dia':"$"+str(total_tour_dia),
                'total_transporte_dia':"$"+str(total_transporte_dia),
                'cantidad_reservas_dia':cantidad_reservas_dia,
                'aumento_total':aumento_total,
                'porcentaje_aumento_total':porcentaje_aumento_total,
                'aumento_tour':aumento_tour,
                'aumento_transporte':aumento_transporte,
                'total_reserva_dias_departamento': "$"+str(total_reserva_dias_departamento),
                'is_aumento_total':is_aumento_total,
                'is_aumento_total_porcentaje':is_aumento_total_porcentaje,
                'is_aumento_total_tour':is_aumento_total_tour,
                'is_aumento_total_transporte':is_aumento_total_transporte,
                'is_reporte':is_reporte,
                'reporte_day':reporte_day,
                'dia':dia
            }

            return render(request,'admin/reportes_template.html',context)

#####Month
        if(request.POST.get('month')):
            mes=int(datetime.datetime.strptime(request.POST.get('month'), "%Y-%m").strftime("%m"))
            mes_anio=datetime.datetime.strptime(request.POST.get('month'), "%Y-%m").strftime("%B/%Y")
            reservas=Reserva.objects.filter(fecha_fin_reserva__month=mes)
            if(reservas.count()==0):
                mensaje="No existen reservas"
                context={
                'mensaje':mensaje,
                'sin_reservas':True
                }
                return render(request,'admin/reportes_template.html',context)  
            is_reporte=True
            reporte_month=True
            total_mes=0
            total_tour_mes=0
            total_transporte_mes=0
            total_reserva_dias_departamento=0
            for reserva in reservas:
                total_mes=total_mes+reserva.valor_total
                total_tour_mes=total_tour_mes+reserva.valor_tour
                total_transporte_mes=total_transporte_mes+reserva.valor_transporte
                total_reserva_dias_departamento=total_reserva_dias_departamento+reserva.valor_reserva_departamento
            
            cantidad_reservas_mes=reservas.count()

            
            #Semana anterior
            
            mes_anterior=int(datetime.datetime.strptime(request.POST.get('month'), "%Y-%m").strftime('%m'))-1
            reservas_mes_anterior=Reserva.objects.filter(fecha_fin_reserva__month=mes_anterior)
           
            total_mes_ma=0
            total_tour_mes_ma=0
            total_transporte_mes_ma=0
            for reserva in reservas_mes_anterior:
                total_mes_ma=total_mes_ma+reserva.valor_total
                total_tour_mes_ma=total_tour_mes_ma+reserva.valor_tour
                total_transporte_mes_ma=total_transporte_mes_ma+reserva.valor_transporte
            

            total_diferencia_ma=total_mes-total_mes_ma
            total_diferencia_tour_ma=total_tour_mes-total_tour_mes_ma
            total_diferencia_transporte_ma=total_transporte_mes-total_transporte_mes_ma


            aumento_total=""
            porcentaje_aumento_total=0
            is_aumento_total=False
            is_aumento_total_porcentaje =False
            if(total_diferencia_ma>=0):
                is_aumento_total=True
                is_aumento_total_porcentaje=True
                aumento_total= "+$"+str(total_diferencia_ma)
                porcentaje_aumento_total=str(   round(-1*(((total_mes_ma*100)/total_mes)-100),2)   )  +"%"
            else:
                is_aumento_total=False
                is_aumento_total_porcentaje=False
                aumento_total= "$"+str(total_diferencia_ma)
                porcentaje_aumento_total= str(-round((round((total_mes_ma*100)/total_mes,2))-100,2)  )+"%"

            aumento_tour=""
            is_aumento_total_tour=False
            if(total_diferencia_tour_ma>=0):
                is_aumento_total_tour=True
                aumento_tour="+$"+str(total_diferencia_tour_ma)
            else:
                is_aumento_total_tour=False
                aumento_tour=total_diferencia_tour_ma
            
            aumento_transporte=""
            is_aumento_total_transporte=False
            if(total_diferencia_transporte_ma>=0):
                is_aumento_total_transporte=True
                aumento_transporte="+$"+str(total_diferencia_transporte_ma)
            else:
                is_aumento_total_transporte=False
                aumento_transporte=total_diferencia_transporte_ma
            #Fin semama anterior


            context={
                'total_mes':total_mes,
                'total_tour_mes':"$"+str(total_tour_mes),
                'total_transporte_mes':"$"+str(total_transporte_mes),
                'cantidad_reservas_mes':cantidad_reservas_mes,
                'aumento_total':aumento_total,
                'porcentaje_aumento_total':porcentaje_aumento_total,
                'aumento_tour':aumento_tour,
                'aumento_transporte':aumento_transporte,
                'total_reserva_dias_departamento': "$"+str(total_reserva_dias_departamento),
                'is_aumento_total':is_aumento_total,
                'is_aumento_total_porcentaje':is_aumento_total_porcentaje,
                'is_aumento_total_tour':is_aumento_total_tour,
                'is_aumento_total_transporte':is_aumento_total_transporte,
                'is_reporte':is_reporte,
                'reporte_month':reporte_month,
                'mes_anio':mes_anio
            }

            return render(request,'admin/reportes_template.html',context)

def is_reserva(reservas,request):
    if(reservas.count()==0):
        mensaje="No existen reservas"
        context={
                'mensaje':mensaje,
                'sin_reservas':True
                }
        return render(request,'admin/reportes_template.html',context)       
        
        

        
    

    