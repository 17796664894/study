# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 14:19
# @Author  : fenfei.liu
# @Email   : 17796664894@163.com
# @File    : test_login.py
from common.read_yaml import read_yaml
import pytest
import requests
from cases.common_function import get_test_data

# 获取测试数据
test_data = get_test_data("login/login_data.yaml")["login_data"]


# 参数化
@pytest.mark.parametrize("test_input", test_data)
@pytest.mark.login
def test_post_login(base_url, test_input):
    _url = "{}/login".format(base_url)
    body = {"username": test_input["username"], "password": test_input["password"]}
    res = requests.post(url=_url, data=body)
    assert res.json().get("message") == test_input["message"]

