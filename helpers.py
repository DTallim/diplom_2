import string
import random
import requests
import data as dt
from urls import BASE_URL, REGISTR_USER_URL, LOGIN_USER_URL

def create_random_string(lenth):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(lenth))
    return random_string

def reg_user():
    user_date = []
    email = f'{create_random_string(8)}@yandex.ru'
    password = create_random_string(12)
    name = create_random_string(12)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f'{BASE_URL}{REGISTR_USER_URL}', data=payload)
    access_token = response.json()["accessToken"]
    refresh_token = response.json()["refreshToken"]

    if response.status_code == 200:
        user_date.append(email)
        user_date.append(password)
        user_date.append(name)
        user_date.append(access_token)
        user_date.append(refresh_token)
    return user_date

def get_private_token():
    private_token = []
    response = requests.post(f'{BASE_URL}{LOGIN_USER_URL}', json={"email": dt.test_email,
                                                                    "password": dt.test_password})
    access_token = response.json()["accessToken"]
    refresh_token = response.json()["refreshToken"]
    if response.status_code == 200:
        private_token.append(access_token)
        private_token.append(refresh_token)
    return private_token