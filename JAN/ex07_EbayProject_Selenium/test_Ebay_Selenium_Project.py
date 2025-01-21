import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Print the Titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")
def test_ebay():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box_input_xpath = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    # search_box_inout_css = driver.find_element(By.CSS_SELECTOR,"#gh-ac")

    search_box_input_xpath.send_keys("macmini")

    search_box_button = driver.find_element(By.XPATH, "//span[@class='gh-search-button__label']")
    search_box_button.click()

    # //div[@class="s-item__title"] -> div.s-item__title

    list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_of_items_prize = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")

    for items in list_of_items:
        print(items.text)

    for items_prize in list_of_items_prize:
        print(items_prize.text)
