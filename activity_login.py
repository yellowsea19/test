#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/14 0014
from selenium import webdriver
import config
import time
class activity(config.ta):
    def __init__(self):
        self.driver=webdriver.Chrome()
    def Login(self):
        open(self,url)
        # self.driver.implicitly_wait(10)
        # time.sleep(3)
        # # self.driver.find_element_by_xpath('//*[@id="ngform"]/bootstrap-decorator[1]/div/div/input').send_keys(loginname)
        # open()
        # self.driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(password)
        #
        # self.driver.find_element_by_xpath('//*[@id="loginPassword"]').submit()
        # time.sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="ngform"]/bootstrap-decorator[4]/div/input').click()
if __name__=='__main__':
    url='http://admin2.join-inapp.com/public#/login'
    p1=activity()
    p1.Login()


