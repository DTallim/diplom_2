
import allure
import pytest
import data as dt
from conftest import login_user_methods


class TestLoginUser:
    @allure.title("Тест входа зарегистрированного пользователя с корректными данными")
    def test_login_user(self, login_user_methods):
        payloads = dt.auth_payload.copy()
        login_user_methods.login_user(payloads)
        login_user_methods.check_status_code(200)

    @pytest.mark.parametrize('key', ['email', 'password'])
    @allure.title("Тест невозможности входа зарегистрированного пользователя с неверным логином и паролем")
    def test_login_user_validation_error(self, login_user_methods, key):
        payloads = dt.auth_payload.copy()
        payloads[key] = 'Не верные данные'
        login_user_methods.login_user(payloads)
        login_user_methods.check_status_code(401)
        login_user_methods.check_login_error()