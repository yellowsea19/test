#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/14 0014
from selenium import webdriver
from page.activity import activitypage
import unittest

class test_activity(unittest.TestCase):
    def setUp(self):
        self.driver=activitypage(webdriver.Chrome())
        self.driver.login()

    def test_addactivity(self):
        self.driver.activity()


