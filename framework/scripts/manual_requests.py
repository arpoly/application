from cerberus import Validator

from framework.config import acces_token
from framework.checker import check_status_code_200
from framework.client_tool import Client
from framework.methods import add_likes


def add_posts_like_list():
    params = {"type": f"{media_types[0]}", "owner_id": f"{owner_id}", "item_id": f"{item_id[0]}", "filter": "likes",
              "friends_only": "1", "offset": "100", "count": "100",
              "access_token": f"{acces_token}", "v": "5.103"}
    response = Client.post(add_likes, params)
    check_status_code_200(response)

    print(response.json())

    v = Validator()
    v.schema = {"response": {"type": "dict", "schema": {"likes": {"type": "integer"}}}}

    if v.validate(response.json()):
        print("valid data")
    else:
        print('invalid data')
        print(v.errors)


add_posts_like_list()
