import os
import httpx

from dotenv import load_dotenv


def get_city_location(city: str) -> str:
    load_dotenv()

    parameters = {
        'q': city,
        'APPID': f"{os.getenv('API_KEY')}",
        'limit': 5
    }

    r = httpx.get(f'{os.getenv("BASE_DOMAIN")}/geo/1.0/direct', params=parameters)
    country = r.json()[0]['country']
    return country


def get_weather_in_the_city(city: str) -> float:
    load_dotenv()
    country = get_city_location(city)
    parameters = {
        'q': f'{city},{country}',
        'APPID': f"{os.getenv('API_KEY')}",
        'units': 'metric'
    }

    r = httpx.get(f'{os.getenv("BASE_DOMAIN")}/data/2.5/weather', params=parameters)
    temperature = r.json()['main']['temp']
    return temperature
