from page.myhonor import addhonor
from selenium import webdriver
import unittest,time
class test_honor(unittest.TestCase):
    def setUp(self):
        self.driver=addhonor(webdriver.Chrome())

        self.driver.login()

    def tearDown(self):
        self.driver.quit()


    def test_addhonor1(self):#zuopinname=作品名称，honorname=荣誉名称，jieshao=荣誉介绍
        '''新增荣誉'''
        self.driver.newhonor(zuopinname='777',honorname='888')

    def test_delhonor(self):
        '''删除荣誉'''
        self.driver.delhonor()














