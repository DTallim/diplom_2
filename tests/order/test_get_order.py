import allure
import data as dt

class TestGetOrders:

    @allure.title("Тест получения списка заказов авторизованного пользователя")
    def test_get_my_orders_list(self, get_order_methods):
        get_order_methods.get_orders({'Authorization': dt.private_token['accessToken']})
        get_order_methods.check_status_code(200)
        get_order_methods.check_order_list_not_empty()

    @allure.title("Тест невозможности получения списка заказов не авторизованного пользователя")
    def test_error_get_orders_list_with_unauthorized_user(self, get_order_methods):
        get_order_methods.get_orders(None)
        get_order_methods.check_status_code(401)
        get_order_methods.check_error_get_order_with_unauthorized_user()