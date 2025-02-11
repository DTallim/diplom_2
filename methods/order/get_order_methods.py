import allure
from methods.api_manager import APIManager
from urls import ORDERS_URL

class GetOrderMethods(APIManager):

    @allure.step('Получение списка заказов')
    def get_orders(self, token):
        self.get_method(ORDERS_URL, headers=token)

    @allure.step('Проверка, что список закзаов не пустой')
    def check_order_list_not_empty(self):
        assert len(self.get_response_body['orders']) != 0

    @allure.step('Проверка невозможности получения списка заказов не авторизованным пользователем')
    def check_error_get_order_with_unauthorized_user(self):
        assert self.get_error_msg == 'You should be authorised'