from django.shortcuts import render,redirect
import requests
import json
import urllib.request
from pprint import pprint
from django.http import HttpResponseServerError

def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        source =   urllib.request.urlopen('https://openweathermap.org/data/2.5/weather?q='+city+'&appid=b6907d289e10d714a6e88b30761fae22').read()
        source2 = urllib.request.urlopen('https://weather.cit.api.here.com/weather/1.0/report.json?product=alerts&name='+city+'&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg').read()
    
# converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        list_of_data2 = json.loads(source2)
        # print(list_of_data)
       
        
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        
        # print(data)
        print(list_of_data2) 
        if list_of_data2['alerts']['alerts'] == []:
            data2 = {
                "city": str(list_of_data2['alerts']['city']),
                "alerts": "Weather is not extreem in " + city

            }
        # print(list_of_data2)
        else:
            data2 = {
                "city": str(list_of_data2['alerts']['city']),
                "alerts": str(list_of_data2['alerts']['alerts'][0]['description'])

            }
    else:
        data={}
        data2={}


    return render(request,'weather/home.html',{'data':data, 'data2' :data2})


