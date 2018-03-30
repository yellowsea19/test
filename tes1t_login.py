#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/24 0024
import unittest
from selenium import webdriver
from page.login import loginPage,url
import  time
data={'logname':'13418914293','password':'00000000','expect':True}
data1={'logname':'13418914293','password':'000000000','expect':False}
class test_login(unittest.TestCase):
    '''登录测试'''
    def  setUp(self):
        self.driver = loginPage(webdriver.Chrome())

    def tearDown(self):
        self.driver.quit()


    def test_01(self):
        '''输入正确的用户名，正确的密码'''
        self.driver.login(data['logname'],data['password'],data['expect'])
    def test_02(self):
        '''输入正确的用户名，错误的密码'''
        self.driver.login(data1['logname'],data1['password'],data1['expect'])

