#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/24 0024
url='http://admin2.join-inapp.com/public#/login'
from config import  configPage
import time
from selenium import webdriver
class loginPage(configPage):
    usr_loc=("xpath",'//*[@id="ngform"]/bootstrap-decorator[1]/div/div/input')
    psw_loc=('xpath','//*[@id="ngform"]/bootstrap-decorator[2]/div/input[2]')
    button_loc=('xpath','//*[@id="ngform"]/bootstrap-decorator[4]/div/input')
    tip_loc=('xpath','//*[@id="menu10003202"]')

    #
    # def __init__(self, driver):
    #     driver = self.driver
    def input_usr (self,text):
        return  self.send_keys(self.usr_loc,text)
    def input_psw(self,text):
        return  self.send_keys(self.psw_loc,text)
    def click_button(self):
        return  self.click(self.button_loc)
    def get_tip(self):
        t = self.get_text(self.tip_loc)
        return t
    def success(self):
        try:
            result= self.get_tip()
            print(result)
            if result == '首页':
                result = True
                return True
            else:
                return False
        except:
            result = False
            return  result




if __name__=='__main__':
    driver=webdriver.Chrome()
    logindriver=loginPage(driver)
    logindriver.open(url)
    logindriver.input_usr('13418914293')
    logindriver.input_psw('00000000')
    logindriver.click_button()
    time.sleep(2)
    logindriver.click_button()
    time.sleep(2)
    f= logindriver.success()
    print(f)
    # try:
    #     f=logindriver.get_tip()
    #     if f=='首页':
    #         f=True
    #         print(f)
    #     else:
    #         print(False)
    # except:
    #     f='123'
    #     print(f)









