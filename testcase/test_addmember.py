import unittest
from selenium import webdriver
from page.member import member
class addmember(unittest.TestCase):
    def setUp(self):
        self.driver=member(webdriver.Chrome())
        self.driver.login(loginname=13499999999,password=11111111)

    def tearDown(self):
        self.driver.quit()

    def test_addmember(self):
        '''新增人员'''
        self.driver.addmember(loginname='15212341234')
    def test_delmember(self):
        '''删除人员'''
        self.driver.delmember()
