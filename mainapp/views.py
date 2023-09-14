from django.shortcuts import render
from datetime import datetime
import requests
from localizaciones.models import locations
import os
from .functions import get_location,hallar_datos

# Create your views here.

def index(request,location = "Bogotá"):
    if request.method == 'POST':
        location = request.POST.get('lugar')
    location2 = locations.objects.values('nombre','code','pais')
    location,ciudad,pais = get_location(location,location2)
    dia = datetime.today()
    hora = datetime.now()
    temperatura,clima,humedad,presion,viento,dias_forecast,temp_forecast = hallar_datos(location)
    dic_clima = {"Clouds":["Nubes","nube.png"],"Rain":["Lluvia","lluvia.png"],"Clear":["Despejado","sol.png"],"Mist":["Neblina","nube.png"]}
    imagen_clima = f"static/images/{dic_clima[clima][1]}"
    clima = dic_clima[clima][0]
    
    return render(request,'inicio.html',{
        'dia':dia,
        'hora':hora,
        'temp':temperatura,
        'clima':clima,
        'humedad':humedad,
        'presion':presion,
        'viento':viento,
        'imagen_clima':imagen_clima,
        'ciudad':ciudad,
        'pais':pais,
        'dias_forecast':dias_forecast,
        'temp_forecast':temp_forecast,
    })

