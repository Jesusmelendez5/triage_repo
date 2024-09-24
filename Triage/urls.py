from django.urls import path
from . import views

urlpatterns = [
    path('', views.triage_inicio, name='inicio'),
    path('signos_vitales/', views.registrar_signos_vitales, name='registrar_signos_vitales'),
    path('triage/', views.nivel_triage_lista, name='nivel_triage_lista'),
    path('triage/<int:pk>/', views.nivel_triage_detalle, name='nivel_triage_detalle'),
   ]