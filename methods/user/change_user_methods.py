import allure
from methods.api_manager import APIManager
from urls import USER_URL


class ChangeUserMethods(APIManager):

    @allure.step('Изменения данных пользователя')
    def patch_user(self, header, payload):
        self.patch_method(USER_URL, headers=header, json=payload)

    @allure.step('Проверка, что данные изменились')
    def check_user_data_change(self, expected_data):
        assert self.get_response_body['user'] == expected_data, (
            f"Фактический результат {self.get_response_body['user']} != {expected_data}")

    @allure.step('Проверка невозможности изменения данных не авторизованным пользователем')
    def check_error_change_data_without_authorization(self):
        assert self.get_error_msg == 'You should be authorised'