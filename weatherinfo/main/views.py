from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    city = request.GET.get('city', 'New Delhi')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=300f35184096401e3b61a1e14e2f9a07'
    city_weather = requests.get(url).json()
    
    # if request.method == 'POST':
    weather_data = {
            'city': city,
            'weather': city_weather['weather'][0]['main'],
            'icon': city_weather['weather'][0]['icon'],
            'kelvin_temp': city_weather['main']['temp'],
            'celcius_temp': int(city_weather['main']['temp'] - 273.15),
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'description': city_weather['weather'][0]['description'],   
        }
   

    context = {'weather_data': weather_data} 
    print(context)
    return render(request, 'index.html', context)
