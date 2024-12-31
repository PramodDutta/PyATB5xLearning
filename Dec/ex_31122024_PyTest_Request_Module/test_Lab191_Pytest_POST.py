import pytest
import allure
import requests


# pip install pytest allure requests

# To make Request

@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"
    # base_path_put = "/booking/1"

    full_url = base_url + base_path_post
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url, headers=headers, json=payload)

    # Status Code Verification
    assert response_data.status_code == 200

    # Booking ID > 0, firstname == Jim
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    print(bookingid)

    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = response_data_json["booking"]["firstname"]
    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    depositpaid = response_data_json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    # https: // jsonpathfinder.com
    #x.booking.bookingdates.checkin
    #response_data_json["booking"]["bookingdates"]["checkin"]

    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout = response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time = response_data.elapsed.total_seconds()
    assert time < 3


@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("Verify that invalid payload Booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"

