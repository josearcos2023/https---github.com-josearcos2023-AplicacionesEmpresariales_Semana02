from django.shortcuts import render
import math

# Create your views here.
def index(request):
    return render(request, 'encuesta/formulario0.html')

def calculadora(request):
    return render(request, 'encuesta/formulario.html')

def resultado1(request):

    operacion = request.POST.get('operacion')
    valor1 = int(request.POST.get('valor1', 0))
    valor2 = int(request.POST.get('valor2', 0))
    resultado = 0

    if operacion=='suma':
        resultado = valor1 + valor2

    elif operacion=='resta':
        resultado = valor1 - valor2

    elif operacion=='multiplicacion':
        resultado = valor1 * valor2

    elif operacion=='division':
        resultado = valor1 / valor2

    context = {
        'valor1': valor1,
        'valor2': valor2,
        'resultado': resultado,
        'operacion': operacion,
    }

    return render(request,'encuesta/resultado.html',context)

def cilindro (request):
    return render(request, 'encuesta/formulario2.html')

def resultado2(request):
    diametro=int(request.POST['diametro'])
    altura=int(request.POST['altura'])
    resultado2=math.pi*pow((diametro)/2,2)*altura

    context={   
        'resultado2':resultado2,
    }
    
    return render(request,'encuesta/resultado2.html',context)