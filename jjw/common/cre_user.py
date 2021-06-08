# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 11:04
# @Author  : fenfei.liu
# @Email   : 17796664894@163.com
# @File    : cre_user.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @author:yue.lu
# @time:2021-05-24
# 用于批量生成建交委用户


import requests, json
import sys
import random


def parameter_setting():
    global total_num, ip
    total_num = 50  # 新建多少个用户
    ip = "10.40.59.15"  # 环境的IP


def post_login():
    global s
    s = requests.Session()
    url = "http://{}:11188/login".format(ip)
    multidata = {
        "username": "admin",  # 账号  登陆不成功时请换个账号
        "password": "0192023a7bbd73250516f069df18b500"  # 密码：admin123
    }
    res = s.post(url=url, data=multidata)


def get_neighborhood():
    # 获取管辖区域ID
    global NeighborhoodId
    NeighborhoodId = []
    url = "http://{}:11188/event/v2/app/neighborhood".format(ip)
    res = s.get(url=url)
    if res.status_code == 200:
        for item in json.loads(res.text)["result"]:
            neighborhood_id = item["neighborhood_id"]
            NeighborhoodId.append(neighborhood_id)


def get_role():
    # 获取角色ID
    global RoleID
    RoleID = []
    url = "http://{}:11188/event/v2/authority/role".format(ip)
    res = s.get(url=url)
    if res.status_code == 200:
        for item in json.loads(res.text)["result"]:
            role_id = item["id"]
            RoleID.append(role_id)


def put_user():
    create_url = "http://{}:11188/event/v2/authority/user".format(ip)
    i = 1
    while i <= total_num:
        username = "user" + str(i)
        create_user_body = {
            "username": username,
            "password": "0192023a7bbd73250516f069df18b500",  # 密码统一123456
            "name": "依图" + str(i),
            "organization": "陆家嘴",
            "roleId": random.sample(RoleID, 1)[0],
            "neighborhoodIds": random.sample(NeighborhoodId, 5)
        }
        res = s.put(create_url, json=create_user_body)
        if res.status_code == 200:
            print("新建用户成功。账号：{}".format(username))
        i += 1


if __name__ == '__main__':
    parameter_setting()
    post_login()
    get_neighborhood()
    get_role()
    put_user()
