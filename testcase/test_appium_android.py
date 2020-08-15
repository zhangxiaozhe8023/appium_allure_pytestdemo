#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-13 08:40
# @Author : apple
# @Software: PyCharm
from time import sleep

import yaml
from appium import webdriver

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

with open("./filesdatas/aa.yml") as f:
    datas  = yaml.safe_load(f)
class Testcart:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "jjj"
        caps["appPackage"] = "com.dangdang.buy2"
        caps["appActivity"] = ".activity.ActivityMainTab"
        caps["noReset"] = "True"
        caps["ensureWebviewsHavePages"] = True
        # 局部变量设置为实例变量用.self

        self.driver = webdriver.Remote ( "http://localhost:4723/wd/hub", caps )
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit ()


    @pytest.mark.parametrize('searchkey',datas)
    def testcast1(self,searchkey):


        el1 = self.driver.find_element(MobileBy.ID ,"com.dangdang.buy2:id/home_view_flipper" )
        el1.click ()
        el2 = self.driver.find_element (MobileBy.ID, "com.dangdang.buy2:id/et_search" )
        el2.send_keys ( searchkey )
        el3 = self.driver.find_element (MobileBy.XPATH,
            f"//*[@text='{searchkey}' and contains(@resource-id,'tv_sug')]" )
        el3.click ()
        el4 = self.driver.find_elements (MobileBy.ID,
            "com.dangdang.buy2:id/product_img_iv" )[0]
        el4.click ()
        el5 =self. driver.find_element_by_id ( "com.dangdang.buy2:id/ll_magic_btn_right" )
        el5.click ()
        sleep(2)
        print(self.driver.page_source)
        el6 = self.driver.find_element(MobileBy.XPATH,"//*[@class = 'android.widget.Toast']")
        assert el6.text =='商品已成功加入购物车'



