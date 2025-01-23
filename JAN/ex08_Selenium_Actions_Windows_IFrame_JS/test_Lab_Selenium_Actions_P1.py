import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Actions P1")
@allure.description("Verify Actions p1")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    firdst_name = driver.find_element(By.XPATH, "//input[@name='firstname']")

    actions = ActionChains(driver=driver)
    (actions
     .key_down(Keys.SHIFT)
     .send_keys_to_element(firdst_name, "the testing academy")
     .key_up(Keys.SHIFT)
     .perform())

    time.sleep(10)
    driver.quit()
