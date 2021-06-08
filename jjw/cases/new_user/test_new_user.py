# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 16:29
# @Author  : fenfei.liu
# @Email   : 17796664894@163.com
# @File    : test_new_user.py
import pytest
import requests
from cases.common_function import get_test_data

test_data = get_test_data("new_user/new_user_data.yaml")["new_user"]


@pytest.mark.parametrize("test_input", test_data)
def test_put_cuser(base_url, test_input, s):
    _url = "{}/event/v2/authority/user".format(base_url)
    body = {"username": test_input["username"], "password": test_input["password"],
            "name": test_input["username"], "roleId": "604045bc46850c27dd6a1540", "neighborhoodIds": []}
    res = s.put(url=_url, json=body)
    assert res.json().get("message") == test_input["message"]



