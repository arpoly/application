import requests as r

from src.utils.constants import VK_HOST


class Client:

    @classmethod
    def get(cls, path: str, params):
        return r.get(url=VK_HOST + path, params=params)

    @classmethod
    def post(cls, path: str, params):
        return r.post(url=VK_HOST + path, params=params,
                      headers={"Content-type": "application/json; charset=UTF-8"})
