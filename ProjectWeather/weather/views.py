from django.shortcuts import render
from requests import request, get
from datetime import datetime

def index(request):
    appid = 'd74f42ecfaf3dfd799b232e7020f48e9'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Moscow'
    res = get(url.format(city)).json()
    time_now = datetime.now()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'description': res['weather'][0]['description'],
        'time': time_now.time()

    }
    print(res)
    contex = {'info': city_info}
    return render(request, 'weather/index.html', contex)