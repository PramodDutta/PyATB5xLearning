import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Actions P2")
@allure.description("Verify MouseBack")
def test_verify_action_mouse():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    atag = driver.find_element(By.ID, "click")
    atag.click()

    actions_builders = ActionBuilder(driver=driver)
    actions_builders.pointer_action.pointer_up(MouseButton.BACK)
    actions_builders.perform()

    time.sleep(10)
    driver.quit()

