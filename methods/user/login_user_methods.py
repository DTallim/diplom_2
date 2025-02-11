import allure
from methods.api_manager import APIManager
from urls import LOGIN_USER_URL, DELETE_USER_URL


class LoginUserMethods(APIManager):
    @allure.step('Вход в личный кабинет зарегистрированным пользователем')
    def login_user(self, payload):
        self.post_method(LOGIN_USER_URL, data=payload)

    @allure.step('Получение ошибки при неправильно набранных полях входа в личный кабинет')
    def check_login_error(self):
        assert self.get_error_msg == "email or password are incorrect"

    @allure.step('Удаление пользователя')
    def delete_user(self):
        self.delete_method(DELETE_USER_URL)
