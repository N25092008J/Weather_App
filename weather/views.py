import requests

import json

from .models import cities

from .forms import user_input

from django.shortcuts import render

def index(request):

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=8bf0f9400af99058ed5fbfa9437ee35f"

    if request.method == "POST":

        forms = user_input(request.POST)

        forms.save()

    forms = user_input()

    city_name = cities.objects.all()

    city_weather = []

    for CITY in city_name:

        a = requests.get(url.format(CITY)).json()

        city_data = {'city':CITY.City.capitalize(),'temp':round((a['main']['temp']) - 273.15),'desc':a['weather'][0]['description'],'icon':a['weather'][0]['icon']}

        if len(city_weather) >= 1:
        
            for i in city_weather:

                print(i)

                if i['city'] == city_data['city']:

                    break

                else:

                    city_weather.append(city_data)

        else:

            city_weather.append(city_data)

    send_html = {'city_weather':city_weather,'forms':forms}

    return render(request,"weather/weather.html",send_html)