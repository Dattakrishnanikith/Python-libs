  
import requests

city = 'Rajahmundry' 

url = 'http://api.weatherapi.com/v1/current.json?key=251629de978e4f5abd9144412251810 &q='+city+'&aqi=no'

response = requests.get(url)

weather_json = response.json()

temp = weather_json.get('current').get('temp_f')

description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description,'and', temp,'degrees' )