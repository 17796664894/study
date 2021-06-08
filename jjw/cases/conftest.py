# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 13:12
# @Author  : fenfei.liu
# @Email   : 17796664894@163.com
# @File    : conftest.py
import pytest
import requests
import os
from common.read_yaml import read_yaml
from cases.common_function import login


# 登录
@pytest.fixture(scope="session", name="s")
def login_user(base_url):
    # 前置操作
    s = requests.Session()
    login(s, base_url)
    yield s
    # 后置操作
    s.close()


# 未登录
@pytest.fixture(name="unlogin")
def unlogin():
    s = requests.Session()
    yield s
    s.close()



