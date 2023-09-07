from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('calculadora', views.calculadora, name='calculadora'),
    path('cilindro', views.cilindro, name='cilindro'),
    path('resultado', views.resultado1, name='resultado'),
    path('resultado2', views.resultado2, name='resultado2'),
]
