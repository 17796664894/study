# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 13:13
# @Author  : fenfei.liu
# @Email   : 17796664894@163.com
# @File    : common_function.py
import pytest
import hashlib
import os
import requests
from common.read_yaml import read_yaml


def get_md5(parmStr):
    # 1、参数必须是utf8
    # 2、python3所有字符都是unicode形式，已经不存在unicode关键字
    # 3、python3 str 实质上就是unicode
    if isinstance(parmStr, str):
        # 如果是unicode先转utf-8
        parmStr = parmStr.encode("utf-8")
    m = hashlib.md5()
    m.update(parmStr)
    return m.hexdigest()


# 获取带cookie headers
def login(s, base_url):
    _url = "{}/login".format(base_url)
    body = {"username": "admin", "password": "0192023a7bbd73250516f069df18b500"}
    res = s.post(url=_url, data=body)
    cookie = {"Cookie": res.headers["Set-Cookie"]}
    s.headers.update(cookie)
    return s


# 获取测试数据路径
def get_test_data(file):
    file_path = os.path.join(os.path.dirname(__file__), file)
    test_data = read_yaml(file_path)
    return test_data


