from django.contrib import admin
from Triage.models import Paciente,SignosVitales,NivelTriage,Triage
# Register your models here.

admin.site.register(Paciente)
admin.site.register(SignosVitales)
admin.site.register(NivelTriage)
admin.site.register(Triage)