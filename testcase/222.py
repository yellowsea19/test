#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/17 0017
from selenium import webdriver
import time
driver=webdriver.Chrome()
def Login(url,loginname,password):

    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ngform"]/bootstrap-decorator[1]/div/div/input').send_keys(loginname)
    driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginPassword"]').submit()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ngform"]/bootstrap-decorator[4]/div/input').click()
if __name__=='__main__':
    url='http://admin2.join-inapp.com/public#/login'
    # p1=activity()
    Login(url,'13418914293','00000000')