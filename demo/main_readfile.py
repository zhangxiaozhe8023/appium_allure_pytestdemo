#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-14 11:48
# @Author : apple
# @Software: PyCharm
import allure
import pytest
import yaml

import yaml


if __name__ == '__main__':
        with open (f'./filesdatas/aa.yml' ) as f:
            datas =yaml.safe_load(f)
            print(datas)
