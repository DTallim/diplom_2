import pytest
import requests
from methods.user.registration_user_methods import RegistrationUserMethods
from methods.user.delete_user_methods import DeleteUserMethods
from methods.user.login_user_methods import LoginUserMethods
from methods.user.change_user_methods import ChangeUserMethods
from methods.order.create_order_methods import CreateOrderMethods
from methods.order.get_order_methods import GetOrderMethods


@pytest.fixture(scope='function')
def registration_user_methods():
    registration_user_methods = RegistrationUserMethods()
    yield registration_user_methods
    delete_user_methods = DeleteUserMethods()
    if registration_user_methods.get_auth_token():
        delete_user_methods.delete_user({'Authrization': registration_user_methods.get_auth_token()})

@pytest.fixture()
def login_user_methods():
    login_user_methods = LoginUserMethods()
    return login_user_methods

@pytest.fixture()
def change_user_methods():
    change_user_methods = ChangeUserMethods()
    return change_user_methods

@pytest.fixture()
def create_order_methods():
    create_order_methods = CreateOrderMethods()
    return create_order_methods

@pytest.fixture()
def get_order_methods():
    get_order_methods = GetOrderMethods()
    return get_order_methods