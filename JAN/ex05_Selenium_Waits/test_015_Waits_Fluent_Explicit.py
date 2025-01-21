import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *


@allure.title("App.vwo.com Implicit Wait")
@allure.description("Verify that the app.vwo.com is loaded with waits")
def test_negative_app_vwo_com():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # driver.implicitly_wait(5) -> 0.01%

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("password@1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    # Wait for the error message

    # A Condition to check the element
    # error_msg_element - comes after 2-4 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # element is visible then assertion
    # when  this -> then do this

    # Smart Logic to wait for the element
    # Condition based Logic

    # Verify that message is visible.
    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match</div>

    # time.sleep(5) # Python Int to wait for 5 seconds without any condition.

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

    WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description")))

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
