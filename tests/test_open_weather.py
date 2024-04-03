import os

from dotenv import load_dotenv
from httpx import Response
from respx.plugin import respx_mock

from weather.weather_api import get_city_location, get_weather_in_the_city

load_dotenv()


def test__get_city_location__return_country(respx_mock):
    expected_json_response = [{'country': 'GB'}]
    respx_mock.get(os.getenv('BASE_DOMAIN')).mock(return_value=Response(200, json=expected_json_response))
    assert get_city_location('London') == 'GB'


# How to crate tests if there is another function in get_weather_in_the_city?
def test__get_weather_in_the_city__return_temperature(respx_mock):
    expected_json_response = {"main": {"temp": 22.19}}
    respx_mock.get(os.getenv('BASE_DOMAIN')).mock(return_value=Response(200, json=expected_json_response))
    assert get_weather_in_the_city('London') == 22.19
