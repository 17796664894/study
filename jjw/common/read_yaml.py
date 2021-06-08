# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 13:15
# @Author  : fenfei.liu
# @Email   : 17796664894@163.com
# @File    : read_yaml.py
import yaml
import os


def read_yaml(yaml_file="test"):
    if not os.path.isfile(yaml_file):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yaml_file)
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data
