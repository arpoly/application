import pytest

from framework.checker import *
from framework.client_tool import Client
from framework.constants import ACCESS_TOKEN
from framework.media_data import *
from framework.methods import DELETE_LIKES


@allure.suite("delete.likes:")
class TestDeletelike:

    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    @allure.title('Positive: delete like on community post')
    def test_delete_like_post(self):
        params = {"type": f"{MEDIA_TYPES[0]}", "item_id": f"{ITEM_ID[0]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(DELETE_LIKES, params)
        check_status_code_200(response)
        check_delete_like_response(response.json())

    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    @allure.title('Positive: delete like on community comment')
    def test_delete_like_comment(self):
        params = {"type": f"{MEDIA_TYPES[1]}", "item_id": f"{ITEM_ID[1]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(DELETE_LIKES, params)
        check_status_code_200(response)
        check_delete_like_response(response.json())

    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    @allure.title('Positive: delete like on community video')
    def test_delete_like_video(self):
        params = {"type": f"{MEDIA_TYPES[2]}", "item_id": f"{ITEM_ID[2]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(DELETE_LIKES, params)
        check_status_code_200(response)
        check_delete_like_response(response.json())

    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    @allure.title('Positive: delete like on community photo')
    def test_delete_like_photo(self):
        params = {"type": f"{MEDIA_TYPES[3]}", "item_id": f"{ITEM_ID[3]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(DELETE_LIKES, params)
        check_status_code_200(response)
        check_delete_like_response(response.json())

    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    @allure.title('Negative: delete like on invalid community photo')
    def test_delete_like_invalid_elem(self):
        params = {"type": f"{MEDIA_TYPES[3]}", "item_id": "*&%!#(", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(DELETE_LIKES, params)
        check_status_code_200(response)
        check_invalid_body(response.json())
