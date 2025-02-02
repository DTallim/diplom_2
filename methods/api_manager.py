import requests
import allure
from urls import BASE_URL

class APIManager():

    @allure.step('POST запрос')
    def post_method(self, endpoint, **kwargs):
        self.response = requests.post(f'{BASE_URL}{endpoint}', **kwargs)
        return self.response

    @allure.step('DELETE запрос')
    def delete_method(self, endpoint, **kwargs):
        self.response = requests.delete(f'{BASE_URL}{endpoint}', **kwargs)
        return self.response

    @allure.step('PATCH запрос')
    def patch_method(self, endpoint, **kwargs):
        self.response = requests.patch(f'{BASE_URL}{endpoint}', **kwargs)
        return self.response

    @allure.step('GET запрос')
    def get_method(self, endpoint, **kwargs):
        self.response = requests.get(f'{BASE_URL}{endpoint}', **kwargs)
        return self.response

    @property
    def get_response_body(self):
        return self.response.json()

    @property
    def get_error_msg(self):
        return self.get_response_body['message']

    @allure.step('Проверка статус кода')
    def check_status_code(self, code):
        assert self.response.status_code == code