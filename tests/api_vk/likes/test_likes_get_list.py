import pytest

from framework.checker import *
from framework.client_tool import Client
from framework.config import ACCESS_TOKEN
from framework.media_data import *
from framework.methods import GETLIST_LIKES


@allure.suite("get.list:")
class TestGetListLikes:

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @allure.title('Positive: get list on owner post ')
    def test_get_posts_like_list(self):
        params = {"type": f"{MEDIA_TYPES[0]}", "owner_id": f"{OWNER_ID}", "item_id": f"{ITEM_ID[0]}", "filter": "likes",
                  "friends_only": "1", "offset": "100", "count": "100",
                  "access_token": f"{ACCESS_TOKEN}", "v": "5.103"}
        response = Client.post(GETLIST_LIKES, params)
        check_status_code_200(response)
        check_get_list_response(response.json())
        print(response.json())

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @allure.title('Positive: get likes on owner comment')
    def test_get_comment_like_list(self):
        params = {"type": f"{MEDIA_TYPES[1]}", "owner_id": f"{OWNER_ID}", "item_id": f"{ITEM_ID[1]}", "filter": "likes",
                  "friends_only": "1", "offset": "100", "count": "100",
                  "access_token": f"{ACCESS_TOKEN}", "v": "5.103"}
        response = Client.post(GETLIST_LIKES, params)
        check_status_code_200(response)
        check_get_list_response(response.json())
        print(response.json())

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @allure.title('Positive: get likes on owner video')
    def test_get_video_like_list(self):
        params = {"type": f"{MEDIA_TYPES[2]}", "owner_id": f"{OWNER_ID}", "item_id": f"{ITEM_ID[2]}", "filter": "likes",
                  "friends_only": "1", "offset": "100", "count": "100",
                  "access_token": f"{ACCESS_TOKEN}", "v": "5.103"}
        response = Client.post(GETLIST_LIKES, params)
        check_status_code_200(response)
        check_get_list_response(response.json())
        print(response.json())

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @allure.title('Positive: get likes on owner photo')
    def test_get_photo_post_like_list(self):
        params = {"type": f"{MEDIA_TYPES[3]}", "owner_id": f"{OWNER_ID}", "item_id": f"{ITEM_ID[3]}", "filter": "likes",
                  "friends_only": "1", "offset": "100", "count": "100",
                  "access_token": f"{ACCESS_TOKEN}", "v": "5.103"}
        response = Client.post(GETLIST_LIKES, params)
        check_status_code_200(response)
        check_get_list_response(response.json())
        print(response.json())

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @allure.title('Negative: get like on invalid video')
    def test_get_like_invalid_elem(self):
        params = {"type": f"{MEDIA_TYPES[2]}", "item_id": "*&%!#(", "owner_id": f"{OWNER_ID}",
                  "access_token": f"{ACCESS_TOKEN}",
                  "v": "5.103"}
        response = Client.post(GETLIST_LIKES, params)
        check_status_code_200(response)
        check_invalid_body_get_list(response.json())
        print(response.json())
