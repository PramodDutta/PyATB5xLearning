import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests


def test_selenium(launch_browser, close_browser):
    launch_browser
    print("Do Tc")
    close_browser