import os
import httpx

from dotenv import load_dotenv


def get_city_location(city):
    load_dotenv()

    parameters = {
        'q': city,
        'APPID': f"{os.getenv('API_KEY')}",
        'limit': 5
    }

    r = httpx.get(f'{os.getenv("BASE_DOMAIN")}/geo/1.0/direct', params=parameters)
    return r.json()[0]['country']



def get_weather_in_the_city(city):
    load_dotenv()
    country = get_city_location(city)
    parameters = {
        'q': f'{city},{country}',
        'APPID': f"{os.getenv('API_KEY')}",
        'units': 'metric'
    }

    r = httpx.get(f'{os.getenv("BASE_DOMAIN")}/data/2.5/weather', params=parameters)

    return f"{r.json()['main']['temp']} °C"
