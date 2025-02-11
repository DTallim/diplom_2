import allure
import pytest
import data as dt

class TestChangeUser:

    @allure.title("Тест изменения данных авторизованного пользователя")
    def test_edit_user_data(self, change_user_methods):
        change_user_methods.patch_user(dt.patch_user_header, dt.patch_payload)
        change_user_methods.check_status_code(200)
        change_user_methods.check_user_data_change(dt.patch_payload)

    @allure.title("Тест невозможности изменения данных не авторизованного пользователя")
    @pytest.mark.parametrize('key, value', [('name', 'Новое имя'), ('email', dt.create_user_payload['email'])])
    def test_edit_user_data_without_authorization(self, change_user_methods, key, value):
        change_user_methods.patch_user(None, {key: value})
        change_user_methods.check_status_code(401)
        change_user_methods.check_error_change_data_without_authorization()