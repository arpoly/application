# vk-api tests

This repository contains tests for VK API. These tests are written in Python and use pytest as the testing framework.

## Running Tests

To run the tests, follow these steps:

1. Install Python 3:

```
brew install python3
```

2. Install the dependencies by running the following command in the application folder:

```
pip3 install -r requirements.txt
```

3. Set up your VK app API data in `config.py`. You can create a VK app by
   visiting [this link](https://vk.com/editapp?act=create). You need to provide the following information:

```
REDIRECT_URL = "http://localhost/vk-auth"
CLIENT_ID = "Your_Client_ID"
CLIENT_SECRET = "Your_Client_Secret"
```

You also need to obtain an access token. You can do this by following the instructions
at [VK's Implicit Flow User Documentation](https://vk.com/dev/implicit_flow_user). After obtaining the access token, add
it to `config.py`.

Alternatively, you can use the `get_token_selenium.py` script to create an access token automatically.

4. Download the Chrome WebDriver that matches your current Chrome browser version
   from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). After downloading, set the path to the
   WebDriver in `config.py`:

```
CHROME_DRIVER_PATH = "path_to_chromedriver"
```

5. Set your VK user login and password in `config.py`:

```
USER_LOGIN = "Your_Login"
USER_PASSWORD = "Your_Password"
```

6. To run the tests, use the following command:

```
python3 -m pytest tests --alluredir ./reports
```

You can also specify a specific test category to run, for example:

```
pytest -v -m smoke --alluredir ./reports
```

## Generating Allure Report

To generate the Allure report for the tests, follow these steps:

1. Make sure you have Allure installed. If not, install it by running:

```
brew install allure
```

2. Run the following command to generate the report:

```
allure serve ./reports
```

## Next Steps

- Implement logging
- DataClases
- Request Builders
- Env Running 
- Pipeline Integration
- Pre-commit, linters
- Swagger CodeGen Tests

