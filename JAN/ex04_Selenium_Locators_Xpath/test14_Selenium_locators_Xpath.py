from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os


@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with invalid creds.")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_app_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Make')]")
    make_app_btn.click()

    # text() -> Exact Match

    # Partial Text() - contains()
    # //a[contains(text(),'Make Appointment')]
    # //a[contains(text(),'Appointment')]
    # //a[contains(text(),'Make')]
    # //a[contains(text(),'Ma')]
    # //a[contains(text(),'App')] - This may fail if there 1 or more a tag with App.
    # <a rel="https:/google.com"/>

    # //a[starts-with(text(),'Make')]






    time.sleep(5)
    driver.quit()  # close everything.
