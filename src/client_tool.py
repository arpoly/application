import logging
import requests
from src.utils.constants import VK_HOST


class Client:

    @classmethod
    def get(cls, path: str, params: dict = None):
        try:
            response = requests.get(url=VK_HOST + path, params=params)
            response.raise_for_status()
            return response
        except requests.RequestException as error:
            logging.error(f"An error occurred during GET request: {error}")
            return None

    @classmethod
    def post(cls, path: str, params: dict = None):
        try:
            headers = {"Content-type": "application/json; charset=UTF-8"}
            response = requests.post(url=VK_HOST + path, params=params, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as error:
            logging.error(f"An error occurred during POST request: {error}")
            return None
