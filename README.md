# vk-api tests

How to run tests:

    in application folder run:
    python3 -m pytest tests --alluredir ./reports
    or:
    pytest -v -m smoke --alluredir ./reports

Generate allure report:

    allure serve ./reports

Methods:

    likes.add 
    likes.delete
    likes.getList
    likes.isLiked

1.Python setup:

    brew install python3 

2.Install dependencies:

in application folder run:

    pip3 install requirements.txt 

3.Set your app api data in config.py, example:

    1.Create vk app:
    https://vk.com/editapp?act=create
    REDIRECT_URL = "http://localhost/vk-auth"
    CLIENT_ID = "7418578"
    CLIENT_SECRET = "3yx0xzUjzMCFcl5LAieF"
    
    2.Get access token by:
    https://vk.com/dev/implicit_flow_user   
    
      Example request, scope offline mode:
    https://oauth.vk.com/authorize?client_id=7418565&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,wall,pages,offline&response_type=token&v=5.103`
    
     add data in config.py
    
    or create by running get_token_selenium.py

4.Driver:

Download web driver for current Chrome version  
https://sites.google.com/a/chromium.org/chromedriver/downloads

    After download, set current driver path "CHROME_DRIVER_PATH=" in config.py  

5.Set current user data in config.py

    USER_LOGIN = ""
    USER_PASSWORD = ""

Example public:
    https://vk.com/dailywisdom

Whats Next?
    logging
    fixture generator
    scheme validate negative cases
    
    