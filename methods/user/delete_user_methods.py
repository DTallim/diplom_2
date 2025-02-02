import allure
from methods.api_manager import APIManager
from urls import USER_URL

class DeleteUserMethods(APIManager):

    @allure.step('Удаление пользователя')
    def delete_user(self, header):
        self.delete_method(USER_URL, headers=header)