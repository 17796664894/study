# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 11:01
# @Author  : fenfei.liu
# @Email   : 17796664894@163.com
# @File    : del_user.py
import requests


def parameter_setting():
    global ip, port
    ip = "10.40.59.15"
    port = 11188


def post_login():
    global s
    s = requests.Session()
    url = "http://{}:{}/login".format(ip, port)
    body = {"username": "admin", "password": "0192023a7bbd73250516f069df18b500"}
    res = s.post(url=url, data=body)
    assert res.json().get("message") == "login success"


def get_user():
    _url = "http://{}:{}/event/v2/authority/user".format(ip, port)
    res = s.get(url=_url)
    return res.json()


def del_user():
    for i in get_user()["result"]:
        if i["username"] not in ["admin", "qwe", "kongyiping", "liufenfei"]:
            print(i["username"])
            _url = "http://{}:{}/event/v2/authority/user/{}".format(ip, port, i["id"])
            res = s.delete(_url)
            assert res.json().get("message") == "ok"


if __name__ == '__main__':
    parameter_setting()
    post_login()
    get_user()
    del_user()
