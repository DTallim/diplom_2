import allure
import pytest
import data as dt
import json

class TestCreateOrder:

    @allure.title("Тест создания заказа с ингредиентами авторизованным и не авторизованным пользователем")
    @pytest.mark.parametrize('ingregients, header', [('Антарианский бессмертный краторный бургер', None),
                                                     ('Альфа-сахаридный spicy флюоресцентный бургер',
                                                      {'Authorization': dt.private_token['accessToken']})])
    def test_create_order(self, create_order_methods, ingregients, header):
        create_order_methods.create_order(header, {'ingredients': dt.ingredients[ingregients]})
        response_body = create_order_methods.get_response_body
        create_order_methods.check_status_code(200)
        assert response_body is not None, "Не получен ответ от сервера"
        assert response_body.get('success') is True, "Заказ не был создан успешно"
        create_order_methods.check_order_has_been_created(ingregients)

    @allure.title("Тест создания заказа без ингредиентов авторизованным и не авторизованным пользователем")
    @pytest.mark.parametrize('header', [None, {'Authorization': dt.private_token['accessToken']}])
    def test_create_order_on_empty_ingredients(self, create_order_methods, header):
        create_order_methods.create_order(header, {'ingredients': None})
        response_body = create_order_methods.get_response_body
        create_order_methods.check_status_code(400)
        assert response_body is not None, "Не получен ответ от сервера"
        assert response_body.get('message') == 'Ingredient ids must be provided', "Неверное сообщение об ошибке"
        create_order_methods.check_error_create_order()

    @allure.title("Тест создания заказа с ингредиентами, имеющими некорректный хеш")
    @pytest.mark.parametrize('header', [None, {'Authorization': dt.private_token['accessToken']}])
    def test_create_order_on_invalid_hash_ingredients(self, create_order_methods, header):
        create_order_methods.create_order(header, {'ingredients': dt.ingredients['not correct hash']})
        create_order_methods.check_status_code(500)
        try:
            response_body = create_order_methods.get_response_body
            error_message = str(response_body)
        except json.JSONDecodeError:
            # Если ответ не является валидным JSON, получаем текст ответа напрямую
            error_message = create_order_methods.response.text
        assert 'Internal Server Error' in error_message, "Неверное сообщение об ошибке для некорректного хеша"