import allure
import pytest
import data as dt

class TestRegistrationUser:

    @allure.title("Тест регистрации пользователя с корректными данными")
    def test_registration_user(self, registration_user_methods):
        registration_user_methods.registration_user(dt.create_user_payload)
        registration_user_methods.check_status_code(200)
        registration_user_methods.check_registration_user_successfully()

    @allure.title("Тест вывода ошибки при регистрации пользователя без почты, логина или пароля")
    @pytest.mark.parametrize('key', ["email", "password", "name"])
    def test_registration_user_validation_error_on_empty_required_fields(self, registration_user_methods, key):
        payload = dt.create_user_payload.copy()
        payload[key] = None
        registration_user_methods.registration_user(payload)
        registration_user_methods.check_status_code(403)
        registration_user_methods.check_registration_error()

    @allure.title("Тест невозможности зарегистрировать пользователя, который уже есть в базе")
    def test_error_on_duplicate_user_registration(self, registration_user_methods):
        registration_user_methods.registration_user(dt.created_user_payload)
        registration_user_methods.check_status_code(403)
        registration_user_methods.check_registration_user_failed()
        registration_user_methods.check_user_already_exist_error()