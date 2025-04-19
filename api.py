import urequests

from lib.env import API_KEY

def get_weather_for(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    
    res = urequests.get(url)
    data = res.json()
    res.close()

    return data['current']['temp_c']
