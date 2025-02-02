import allure
from methods.api_manager import APIManager
from urls import REGISTR_USER_URL

class RegistrationUserMethods(APIManager):

    @allure.step('Регистрация нового пользователя')
    def registration_user(self, payload):
        self.post_method(REGISTR_USER_URL, data=payload)

    @allure.step('Получение токена')
    def get_auth_token(self):
        response_body = self.get_response_body
        if 'accessToken' in response_body:
            return response_body['accessToken']
        else:
            return None

    @allure.step('Проверка успешности регистрации пользователя')
    def check_registration_user_successfully(self):
        assert self.get_response_body['success'] == True

    @allure.step('Проверка, что пользователь не зарегистрирован')
    def check_registration_user_failed(self):
        assert self.get_response_body['success'] == False

    @allure.step('Получение сообщения ошибки регистрации пользователя')
    def check_registration_error(self):
        assert self.get_error_msg == "Email, password and name are required fields", \
            f'Фактический результат {self.get_error_msg}'

    @allure.step('Получение сообщения ошибки, что такой пользователь уже зарегистрирован')
    def check_user_already_exist_error(self):
        assert self.get_error_msg == "User already exists", \
            f'Фактический результат {self.get_error_msg}'