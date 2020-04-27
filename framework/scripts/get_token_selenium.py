#!/usr/bin/env python3

import urllib
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from framework.config import CLIENT_ID, GET_TOKEN_URL, DRIVER_PATH, REDIRECT_URL, USER_LOGIN, USER_PASSWORD


# @pytest.fixture(scope="session")
# @allure.step("Get access token")
def access_token():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(f"{DRIVER_PATH}", options=options)
    url = f"{GET_TOKEN_URL}?client_id={CLIENT_ID}&display=page&redirect_uri={REDIRECT_URL}&scope=wall,post&response_type=token&v=5.103"
    driver.get(url=url)
    driver.find_element_by_xpath('//*[@id="login_submit"]/div/div/input[6]').send_keys(f"{USER_LOGIN}")
    driver.find_element_by_xpath('//*[@id="login_submit"]/div/div/input[7]').send_keys(f"{USER_PASSWORD}")
    driver.find_element_by_xpath('//*[@id="install_allow"]').click()
    current_url = driver.current_url
    parsed = urlparse(current_url)
    fragment = parsed.fragment
    json_params = dict(urllib.parse.parse_qsl(fragment))
    access_code = json_params["access_token"]
    driver.implicitly_wait("20")
    return print(access_code)


access_token()
