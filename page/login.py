#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/24 0024
import time
from common.config import  configPage,url,loginname,password
class loginPage(configPage):
    usr_loc=("xpath",'//*[@id="ngform"]/bootstrap-decorator[1]/div/div/input')
    psw_loc=('xpath','//*[@id="ngform"]/bootstrap-decorator[2]/div/input[2]')
    button_loc=('xpath','//*[@id="ngform"]/bootstrap-decorator[4]/div/input')
    tip_loc=('xpath','//*[@id="menu10003202"]')
    # def __init__(self):
    #     self.driver=webdriver.Chrome()
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
    def login(self,loginname=loginname,password=password,result=True):
        self.open(url)
        self.input_usr(loginname)
        self.input_psw(password)
        self.click_button()
        time.sleep(2)
        try:
            self.click_button()
        except:pass
        time.sleep(3)



if __name__=='__main__':

    logindriver=loginPage()
    logindriver.login()










