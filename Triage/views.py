from django.shortcuts import render

# Create your views here.

def  triage_inicio(request):
    return render(request, 'inicio.html')  

from django.shortcuts import render, redirect
from .models import SignosVitales, Paciente
from django.http import HttpResponse
from django.contrib import messages

def registrar_signos_vitales(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        paciente_id = request.POST.get('paciente')
        presion_sistolica = request.POST.get('presion_arterial_sistolica')
        presion_diastolica = request.POST.get('presion_arterial_diastolica')
        frecuencia_cardiaca = request.POST.get('frecuencia_cardiaca')
        frecuencia_respiratoria = request.POST.get('frecuencia_respiratoria')
        temperatura = request.POST.get('temperatura')
        saturacion_oxigeno = request.POST.get('saturacion_oxigeno')

        try:
            # Obtener el paciente
            paciente = Paciente.objects.get(id=paciente_id)

            # Crear un nuevo registro de signos vitales
            signos_vitales = SignosVitales.objects.create(
                paciente=paciente,
                presion_arterial_sistolica=presion_sistolica,
                presion_arterial_diastolica=presion_diastolica,
                frecuencia_cardiaca=frecuencia_cardiaca,
                frecuencia_respiratoria=frecuencia_respiratoria,
                temperatura=temperatura,
                saturacion_oxigeno=saturacion_oxigeno
            )
            
            # Guardar los signos vitales
            signos_vitales.save()

            messages.success(request, "Signos vitales guardados exitosamente.")
            return redirect( 'registrar_signos_vitales')  # Redirige a una página después de guardar
        except Paciente.DoesNotExist:
            messages.error(request, "Paciente no encontrado.")
    
    pacientes = Paciente.objects.all()
    signos_vitales = SignosVitales.objects.all()
    
    return render(request, 'plantillas/signos_vitales.html', {
        'pacientes': pacientes,
        'signos_vitales': signos_vitales,
    })

