from selenium import  webdriver
from page.myhonorpage import addhonor,url
from testcase.test_login import test_login
import unittest
class new_honor(unittest.TestCase):
    def setUp(self):
         driver=webdriver.Chrome()
         self.honordriver=addhonor(driver)
         self.honordriver.open(url)
    def test_add(self):
        test_login.login()
        addhonor.my_center_menu()
        addhonor.myhonor()