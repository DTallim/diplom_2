import helpers as hp

test_email = "sukliia_12A@yandex.ru"
test_password = "89299669666"

create_user_payload = {
    "email": f'{hp.create_random_string(8)}@yandex.ru',
    "password": hp.create_random_string(12),
    "name": hp.create_random_string(12)
}

gen_params = hp.reg_user()

created_user_payload = {"email": gen_params[0],
                        "password": gen_params[1],
                        "name": gen_params[2]}

auth_payload = {"email": gen_params[0],
                "password": gen_params[1]}

patch_user_header = {'Authorization': gen_params[3]}

patch_payload  = {"email": gen_params[0].lower(),
                  "name": 'Новое имя'}

ingredients = {
    'Антарианский бессмертный краторный бургер': ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6f"],
    'Альфа-сахаридный spicy флюоресцентный бургер': ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa78"],
    'not correct hash': ["61c0c5566671d1f82001bdaaa6d", "61c0c5966671d1f82001bdaaa72"]
}

private_token = {
    "accessToken": hp.get_private_token()[0],
    "refreshToken": hp.get_private_token()[1]
}