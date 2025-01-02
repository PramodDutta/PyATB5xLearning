import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests


def test_update_req_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)


def test_update_req_2(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)


def test_update_req_3(create_token, create_booking_id, read_csv_file_data):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)