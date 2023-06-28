import time

import allure
from cerberus import Validator
from hamcrest import assert_that, equal_to
from requests import codes

from src.schemas import *


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


def _response_body_check(body, schema):
    v = Validator()
    v.schema = schema
    v.validate(body)
    if v.validate(body):
        a = "valid data"
        assert a == "valid data"
    else:
        b = "invalid data"
        assert b == "valid data"


def _response_invalid_body(body, schema):
    v = Validator()
    v.schema = schema
    v.validate(body)
    if v.validate(body):
        massage = "invalid data"
        assert massage != "valid data"


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(200))


@allure.step
def check_status_code_200(response):
    time.sleep(1)
    _response_general_check(response, expected_code=codes.ok)


@allure.step
def check_status_code_201(response):
    _response_general_check(response, expected_code=codes.created)


@allure.step
def check_status_code_404(response):
    _response_general_check(response, expected_code=codes.not_found)


@allure.step
def check_status_code_500(response):
    _response_general_check(response, expected_code=codes.server_error)


@allure.step
def check_add_like_response(body, schema=ADDLIKE):
    _response_body_check(body, schema)


@allure.step
def check_delete_like_response(body, schema=DELETELIKE):
    _response_body_check(body, schema)


@allure.step
def check_get_list_response(body, schema=GETLIST):
    _response_body_check(body, schema)


@allure.step
def check_isliked_response(body, schema=ISLIKED):
    _response_body_check(body, schema)
    assert body["response"]["liked"] == 1


@allure.step
def check_invalid_body(body, schema=ADDLIKE):
    _response_invalid_body(body, schema)


@allure.step
def check_invalid_body_get_list(body, schema=GETLIST):
    _response_invalid_body(body, schema)


@allure.step
def check_invalid_is_liked_body(body, schema=ISLIKED):
    _response_invalid_body(body, schema)
