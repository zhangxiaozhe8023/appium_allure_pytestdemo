#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-13 08:40
# @Author : apple
# @Software: PyCharm
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
import allure
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Testdangdu:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "jjj"
        caps["appPackage"] = "com.dangdang.buy2"
        caps["appActivity"] = ".activity.ActivityMainTab"
        caps["noReset"] = "True"
        caps["ensureWebviewsHavePages"] = True
        # 局部变量设置为实例变量用.self

        self.driver = webdriver.Remote ( "http://localhost:4723/wd/hub", caps )
        self.driver.implicitly_wait(10)
    def teardown_class(self):
        filename = './filesdatas/tmp.PNG'
        self.driver.save_screenshot(filename)
        allure.attach.file(filename,name ="这是截图",attachment_type=allure.attachment_type.PNG)

        self.driver.quit ()
    # 每次执行用例的时候返点击4次返回键回到首页
    def teardown(self):
        for i in range(4):
            self.driver.back()
    def testcast1(self):


        el1 = self.driver.find_element(MobileBy.ID ,"com.dangdang.buy2:id/tab_category_iv" )
        el1.click ()

        el3 = self.driver.find_element (MobileBy.XPATH,"//*[@text='书单' and @resource-id= 'com.dangdang.buy2:id/tv_tab_title']" )
        el3.click ()

        sleep(5)
        el4 = self.driver.find_elements (MobileBy.ID,"com.dangdang.buy2:id/rv_rich_discovery")[0]
        el4.click ()
        sleep(8)
        el5 =self. driver.find_element_by_id ( "com.dangdang.buy2:id/tv_attention")
        el5.click ()
        # print(self.driver.page_source)
        el6 = self.driver.find_element(MobileBy.XPATH,"//*[@class = 'android.widget.Toast']")
        assert el6.text =='关注成功'
        el7 = self.driver.find_element_by_id ( "com.dangdang.buy2:id/tv_rich_detial_back" )
        el7.click ()
        # 点击右上角的小人
        el8 = self.driver.find_elements ( MobileBy.XPATH,"//*[@class = 'android.widget.TextView' and @resource-id= 'com.dangdang.buy2:id/etv_icon']" )[1]
        el8.click ()
        sleep(5)

        el10 = self.driver.find_element ( MobileBy.XPATH,
                                          "//*[@text='关注' and @resource-id= 'com.dangdang.buy2:id/tv_tab_fan_name']" )
        el10.click ()

        el9 = self.driver.find_element ( MobileBy.ID,
                                         "com.dangdang.buy2:id/v_split")
        el9.click ()
        sleep(5)
        el11 = self.driver.find_element ( MobileBy.ID,
                                         "com.dangdang.buy2:id/follow_tv" )
        el11.click ()

        el10 = self.driver.find_element(MobileBy.XPATH,"//*[@class = 'android.widget.Toast']")
        assert el10.text =='已取消关注'





