import requests


def weather_data(query):
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=0142515b87702fb26174239fb8b60b09&units=metric')
    return res.json()


def temperature(result):
    temp = ("{}°C".format(result['main']['temp']))
    return temp


def wind_speed(result):
    speed = result['wind']['speed']
    return str(speed) + " meter per second"


def Description(result):
    description = result['weather'][0]['description']
    return description


def Weather(result):
    weather = result['weather'][0]['main']
    return weather


city = "islamabad"
query = 'q=' + city
w_data = weather_data(query)
city_temp = temperature(w_data)
city_wind_speed = wind_speed(w_data)
city_disc = Description(w_data)
city_weather = Weather(w_data)
