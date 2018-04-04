#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/14 0014
from selenium import webdriver
from page.activity import activitypage
import unittest,time


class test_activity(unittest.TestCase):
    def setUp(self):
        self.driver=activitypage(webdriver.Chrome())
        self.driver.login()

    def test_addactivity(self):
        '''新增活动'''
        self.driver.activity()

    def test_audit1(self):
        '''一审活动'''
        self.driver.audit1()
    def test_audit2(self):
        '''二审活动'''
        self.driver.audit1()
