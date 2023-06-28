import logging

from cerberus import Validator

from src.checker import check_status_code_200
from src.client_tool import Client
from src.constants import MEDIA_TYPES, ITEM_ID, ADD_LIKES
from src.secrets import ACCESS_TOKEN, OWNER_ID


def add_posts_like_list():
    params = {"type": f"{MEDIA_TYPES[0]}", "owner_id": f"{OWNER_ID}", "item_id": f"{ITEM_ID[0]}", "filter": "likes",
              "friends_only": "1", "offset": "100", "count": "100",
              "access_token": f"{ACCESS_TOKEN}", "v": "5.103"}
    response = Client.post(ADD_LIKES, params)
    check_status_code_200(response)

    v = Validator()
    v.schema = {"response": {"type": "dict", "schema": {"likes": {"type": "integer"}}}}

    if v.validate(response.json()):
        logging.info("valid data")
    else:
        logging.info('invalid data')
