from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    documento_identidad = models.CharField(max_length=20, unique=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class SignosVitales(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='signos_vitales')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    presion_arterial_sistolica = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)])
    presion_arterial_diastolica = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    frecuencia_cardiaca = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)])
    frecuencia_respiratoria = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)
    saturacion_oxigeno = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"Signos vitales de {self.paciente} - {self.fecha_hora}"

class NivelTriage(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    color = models.CharField(max_length=50, choices=[('R', 'Rojo'), ('N', 'Naranja'), ('A', 'Amarillo'),('V','Verde'),('Az','Azul')])
    tiempo_maximo_atencion = models.IntegerField(help_text="Tiempo máximo de atención en minutos")

    def __str__(self):
        return self.nombre

class Triage(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='triages')
    nivel_triage = models.ForeignKey(NivelTriage, on_delete=models.PROTECT)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    motivo_consulta = models.TextField()
    observaciones = models.TextField(blank=True)
    signos_vitales = models.OneToOneField(SignosVitales, on_delete=models.CASCADE)

    def __str__(self):
        return f"Triage de {self.paciente} - Nivel: {self.nivel_triage}"
