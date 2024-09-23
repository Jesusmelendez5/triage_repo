from django.urls import path
from . import views

urlpatterns = [
    path('', views.triage_inicio, name='inicio'),
    path('signos_vitales/', views.registrar_signos_vitales, name='registrar_signos_vitales'),
   ]