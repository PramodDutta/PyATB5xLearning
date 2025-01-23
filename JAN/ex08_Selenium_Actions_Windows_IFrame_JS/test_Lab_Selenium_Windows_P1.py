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


@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_action_windows():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle  # 1
    print(parent_window)  # 104C534CEA415D6AB43D3EADD69D6A0B

    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    window_handles = driver.window_handles  # 2
    print(window_handles)

    # ['845E86EDA913F2F693FA0FED129E8866', 'DD9A2AFB80FBDF5F088C2546BAF09073']

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Test cased Passed")
            break
