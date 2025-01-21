import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.common.by import By


@allure.title("App.vwo.com Implicit Wait")
@allure.description("Verify that the app.vwo.com is loaded with waits")
def test_negative_app_vwo_com():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # driver.implicitly_wait(5)

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("password@1234")





