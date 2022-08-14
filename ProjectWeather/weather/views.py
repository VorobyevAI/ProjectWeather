from django.shortcuts import render
from requests import request, get
from datetime import datetime
from .models import City
from .forms import CityForm

def index(request):
    appid = 'd74f42ecfaf3dfd799b232e7020f48e9'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()


    form = CityForm()

    cities = City.objects.all()
    time_now = datetime.now()
    all_cities = []
    for city in cities:
        res = get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'description': res['weather'][0]['description'],
            'time': time_now.time()

        }
        all_cities.append(city_info)

    contex = {'info': all_cities, 'form': form}
    return render(request, 'weather/index.html', contex)