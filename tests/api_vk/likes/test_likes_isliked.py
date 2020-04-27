import pytest

from framework.checker import *
from framework.client_tool import Client
from framework.config import ACCESS_TOKEN
from framework.media_data import *
from framework.methods import ISLIKED_LIKES


@allure.suite("isLiked.likes:")
class TestIsLiked:

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @allure.title('Positive: check post is liked')
    def test_is_liked_post(self):
        params = {"type": f"{MEDIA_TYPES[0]}", "item_id": f"{ITEM_ID[0]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ISLIKED_LIKES, params)
        check_status_code_200(response)
        check_isliked_response(response.json())
        print(response.json())

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @allure.title('Positive: check comment is liked')
    def test_is_liked_comment(self):
        params = {"type": f"{MEDIA_TYPES[1]}", "item_id": f"{ITEM_ID[1]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ISLIKED_LIKES, params)
        check_status_code_200(response)
        check_isliked_response(response.json())
        print(response.json())

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @allure.title('Positive: check video is liked')
    def test_is_liked_video(self):
        params = {"type": f"{MEDIA_TYPES[2]}", "item_id": f"{ITEM_ID[2]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ISLIKED_LIKES, params)
        check_status_code_200(response)
        check_isliked_response(response.json())
        print(response.json())

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @allure.title('Positive: check photo is liked')
    def test_is_liked_photo(self):
        params = {"type": f"{MEDIA_TYPES[3]}", "item_id": f"{ITEM_ID[3]}", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ISLIKED_LIKES, params)
        check_status_code_200(response)
        check_isliked_response(response.json())
        print(response.json())

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @allure.title('Negative: check invalid comment is liked')
    def test_is_liked_invalid_photo(self):
        params = {"type": f"{MEDIA_TYPES[1]}", "item_id": "A1295612hsgfd", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(ISLIKED_LIKES, params)
        check_status_code_200(response)
        check_invalid_is_liked_body(response.json())
        print(response.json())
