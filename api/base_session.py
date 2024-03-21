import os

from dotenv import load_dotenv
from httpx import Client
from httpx._client import BaseClient

load_dotenv()


class BaseSession(Client):
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        super().__init__(**kwargs)

    # def request(self, method, url, **kwargs):
    #     response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
    #     return response

    def request(self, method, url, **kwargs):
        full_url = f'{self.base_url}{url}'
        response = super().request(method, url=full_url, **kwargs)
        return response


def main_url() -> BaseSession:

    base_domain = 'http://api.openweathermap.org'
    return BaseSession(base_url=base_domain)
