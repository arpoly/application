import pytest

from src.utils.checker import *
from src.client_tool import Client
from src.utils.constants import MEDIA_TYPES, ITEM_ID, ADD_LIKES
from src.utils.secrets import ACCESS_TOKEN, OWNER_ID


@allure.suite("add.likes:")
class TestAddlike:

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @allure.title('Positive: add like on community post')
    def test_add_like_post(self):
        params = {"type": f"{MEDIA_TYPES[0]}", "item_id": f"{ITEM_ID[0]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ADD_LIKES, params)
        check_status_code_200(response)
        check_add_like_response(response.json())

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @allure.title('Positive: add like on community comment')
    def test_add_like_comment(self):
        params = {"type": f"{MEDIA_TYPES[1]}", "item_id": f"{ITEM_ID[1]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ADD_LIKES, params)
        check_status_code_200(response)
        check_add_like_response(response.json())

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @allure.title('Positive: add like on community video')
    def test_add_like_video(self):
        params = {"type": f"{MEDIA_TYPES[2]}", "item_id": f"{ITEM_ID[2]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ADD_LIKES, params)
        check_status_code_200(response)
        check_add_like_response(response.json())

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @allure.title('Positive: add like on community photo')
    def test_add_like_photo(self):
        params = {"type": f"{MEDIA_TYPES[3]}", "item_id": f"{ITEM_ID[3]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ADD_LIKES, params)
        check_status_code_200(response)
        check_add_like_response(response.json())

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @allure.title('Negative: add like on invalid community post')
    def test_add_like_invalid_elem(self):
        params = {"type": f"{MEDIA_TYPES[0]}", "item_id": "*&%!#(", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ADD_LIKES, params)
        check_status_code_200(response)
        check_invalid_body(response.json())
