import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_headers")
    ]

    def setup(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        self.response1 = MyRequests.post("/user/login", data=data)
        self.auth_sid = self.get_cookie(self.response1,"auth_sid")
        self.token = self.get_headers(self.response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(self.response1, "user_id")
       
    def test_auth(self):
        auth_sid = self.response1.cookies.get("auth_sid")
        token = self.response1.headers.get("x-csrf-token")
        response2 = MyRequests.get(
            "/user/auth", 
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth(self, condition):
        if condition == "no_cookie":
            response2 = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response2 = MyRequests.get(
               "/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is authorized with condition {condition}"
        )