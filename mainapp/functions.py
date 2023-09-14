import requests
import matplotlib.pyplot as plt
import seaborn as sns
def get_location(location,location2):
    for i in location2:
        if i['nombre'] == location:
            location = i['code']
            ciudad = i['nombre']
            pais = i['pais']
            return location,ciudad,pais
    return "Bogota","Bogotá","Colombia"

def hallar_datos(location):
    api_location = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid=433a5f675f608a12af9007876a2623af"
    response = requests.get(api_location)
    datos = response.json()
    latitud = datos[0]['lat']
    longitud = datos[0]['lon']
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid=433a5f675f608a12af9007876a2623af&units=metric&lang=es"
    api_url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitud}&lon={longitud}&appid=433a5f675f608a12af9007876a2623af&units=metric&lang=es"
    response = requests.get(api_url)
    datos = response.json()
    response_forecast = requests.get(api_url_forecast)
    datos_forecast = response_forecast.json()
    dic = {}
    dia_actual = datos_forecast['list'][0]['dt_txt'][0:10]
    print(dia_actual)
    for medida in datos_forecast['list']:
        if dia_actual == medida['dt_txt'][0:10]:
            pass
        else:
            dia_actual = medida['dt_txt'][0:10]
        dic[dia_actual] = dic.get(dia_actual,[])
        dic[dia_actual].append(medida['main']['temp'])
    for i in dic.keys():
        dic[i] = round(sum(dic.get(i))/len(dic.get(i)))
    temperatura = round(datos['main']['temp'])
    clima = datos['weather'][0]['main']
    humedad = datos['main']['humidity']
    presion = datos['main']['pressure']
    viento = datos['wind']['speed']
    minimo = min(dic.values())-2
    maximo = max(dic.values())+2
    fig = plt.figure(figsize=(10, 5))
    fig.patch.set_facecolor('#0077be')
    sns.set_theme(style="darkgrid")
    ax = sns.lineplot(y=dic.values(),x=dic.keys(),marker=".",markersize=15,linewidth=2,linestyle="dashed")
    ax.set_xlabel("Fecha",fontsize=15)
    ax.set_ylabel("Temperatura(°C)",fontsize=15)
    for valor,fecha in zip(dic.values(),dic.keys()):
        ax.text(fecha,valor+0.5,str(valor)+"°C", fontsize=20,ha="center") 
    plt.grid(True)
    plt.ylim(minimo,maximo)
    
    plt.savefig("./mainapp/static/images/forecast.png")
    return temperatura,clima,humedad,presion,viento,dic.keys(),dic.values()