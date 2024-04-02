from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from weather.weather_api import get_weather_in_the_city

# TODO 1.Add base session, 2. add errror handler, 3. add

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root() -> dict:
    return {"Hello": "People!"}


@app.get("/weather")
def read_item():
    return r'To get current temperature fill the city in the URL. EXAMPLE: weather/London'


@app.get("/weather/{city}")
def read_item(city: str):
    weather = get_weather_in_the_city(city)
    if weather:
        return weather
    else:
        return 'There is no such city in my list. Please check the spelling and try again'
