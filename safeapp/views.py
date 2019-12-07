from django.shortcuts import render,redirect
import requests
import json
import urllib.request


def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        

    # url='https://weather.cit.api.here.com/weather/1.0/report.json?product=alerts&name={}&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg'.format(city)
        # source = urllib.request.urlopen('https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22').read() 
        source =   urllib.request.urlopen('https://openweathermap.org/data/2.5/weather?q='+city+'&appid=b6907d289e10d714a6e88b30761fae22').read()
        # source = urllib.request.urlopen( 
            # 'https://openweathermap.org/data/2.5/weather?q=' 
                    # + city + '&appid = b6907d289e10d714a6e88b30761fae22').read() 
#   'https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format(city)

# converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    else: 
        data ={} 


    return render(request,'weather/home.html')