import allure
from methods.api_manager import APIManager
from urls import ORDERS_URL


class CreateOrderMethods(APIManager):

    @allure.step('Создание нового заказ')
    def create_order(self, header, payload):
        self.post_method(ORDERS_URL, headers=header, data=payload)

    @allure.step('Проверка, что новый заказ создан')
    def check_order_has_been_created(self, burger):
        assert (self.get_response_body['name'] == burger) and (self.get_response_body['success'])

    @allure.step('Проверка, что заказ не создан')
    def check_error_create_order(self):
        assert self.get_error_msg == 'Ingredient ids must be provided'