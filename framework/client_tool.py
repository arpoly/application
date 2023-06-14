import requests as r

from framework.constants import VK_HOST


class Client:

    @classmethod
    def get(self, path: str, params):
        return r.get(url=VK_HOST + path, params=params)

    @classmethod
    def post(self, path: str, params):
        return r.post(url=VK_HOST + path, params=params,
                      headers={"Content-type": "application/json; charset=UTF-8"})
