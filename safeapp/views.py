from django.shortcuts import render,redirect,HttpResponseRedirect
import requests
import json
import urllib.request


def home(request):
    data={}
    data={}
    if request.method == 'POST':
        
    # Try block to catch 
        city = request.POST['city']

        try:
            # int('sy')
            
            source = requests.get('https://openweathermap.org/data/2.5/weather?q='+city+'&appid=b6907d289e10d714a6e88b30761fae22')
            if not source.status_code//100  == 2:
            
                return redirect('error')  
            source2 = requests.get('https://weather.cit.api.here.com/weather/1.0/report.json?product=alerts&name='+city+'&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg')

    # converting JSON data to a dictionary 
            if source.status_code == 200 and  source2.status_code == 200:
                list_of_data = json.loads(source.content)
                list_of_data2 = json.loads(source2.content)
                print(type(list_of_data),'============================')
                data = {
                "country_code": str(list_of_data['sys']['country']), 
                "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
                "temp": str(list_of_data['main']['temp']) + 'k', 
                "pressure": str(list_of_data['main']['pressure']), 
                "humidity": str(list_of_data['main']['humidity']), 
                }
                if list_of_data2['alerts']['alerts'] == []:
                            data2 = {
                                "city": str(list_of_data2['alerts']['city']),
                                "alerts": "Weather is not extreem in " + city

                            }
            # print(list_of_data2)
                else:
                    data2 = {
                        "city": str(list_of_data2['alerts']['city']),
                        "alerts": str(list_of_data2['alerts']['alerts'][0]['description'] + '. Stay safe')

                    }                
        except requests.exceptions.HTTPError as err:
            print('------------')
            
        except requests.exceptions.RequestException as e:
            print(e)

    return render(request,'weather/home.html',locals())

def error(request):
    return render(request, 'weather/500.html')


