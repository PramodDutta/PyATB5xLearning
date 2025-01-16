import time

from selenium import webdriver
import allure
import pytest


@allure.title("Open the app.vwo.com")
@pytest.mark.regresssion
def test_vwo_login():
    driver = webdriver.Chrome()
    # 1. This code is translated into the API request
    # 2. POST request - browser DRIVER(Server)
    # 3. Where It will create a Session or Fresh copy Browser.(Chrome)
    # 4. Session ID - 16 digit ( 91701488d16e3b7fb1442f7f2e1a8955) will be creared
    driver.get("https://app.vwo.com")
    print(driver.session_id)
    # 5. GET -> GET API request to navigate to particular page
    # 6. browser will navigate to the URL.

    # Source code(Client) -> API Request( W3C) -> Browser Driver(Server) -> Browser
