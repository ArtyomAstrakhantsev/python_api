import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):

    def test_user_create_successfully(self):
        data = self.prepare_reg_data()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_json_have_key(response, "id")
        Assertions.assert_code_status(response, 200)

    def test_create_user_with_existing_email(self):
        
        email = "vinkotov@example.com"
        data = self.prepare_reg_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"