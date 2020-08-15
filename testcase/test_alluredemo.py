#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-14 11:30
# @Author : apple
# @Software: PyCharm
import allure

@allure.testcase('www.baidu.com')
def test01():
        print('ddd')

@allure.testcase('http://allure.qatools.ru/')
def test02():
         print ( '0000' )
@allure.title('这个是可以在测试报告上传图片')
def test03():
    allure.attach.file("./filesdatas/qq.jpg",name='这是图片',attachment_type=allure.attachment_type.PNG)
    print('jjj')

@allure.title ( '这个是可以在测试报告上传视频' )
def testmp4():
    allure.attach.file('./filesdatas/测试的视频.mp4',name='这是视频',attachment_type=allure.attachment_type.MP4)

@allure.title ( '这个是可以在测试报告上传视频' )
def test_text():
    allure.attach('sssss',name='这是文本',attachment_type=allure.attachment_type.TEXT)