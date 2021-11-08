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
            print(reservas)
            return render(request,'admin/reportes_template.html')

        
    

    