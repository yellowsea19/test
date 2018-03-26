#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/24 0024
import unittest
from selenium import webdriver
from loginpage import loginPage,url
import  HTMLTestRunner
import  time
data={'logname':'13418914293','password':'00000000','expect':True}
data1={'logname':'13418914293','password':'000000000','expect':False}
class test_login(unittest.TestCase):
    '''登录测试'''
    def  setUp(self):
        self.driver = webdriver.Chrome()
        self.logindriver = loginPage(self.driver)
        self.logindriver.open(url)
    def tearDown(self):
        self.driver.close()
    def success(self):
        try:
            f = self.logindriver.get_tip()
            return f
        except:
            f = '123'
            return ''
    def login(self,login_name='13418914293',psw='00000000',expect=True):
        self.logindriver.input_usr(login_name)
        self.logindriver.input_psw(psw)
        self.logindriver.click_button()
        time.sleep(2)
        self.logindriver.click_button()
        time.sleep(2)
        text=self.logindriver.success()
        print(text)
        self.assertEqual(text,expect)

    def test_01(self):
        '''输入正确的用户名，正确的密码'''
        self.login(data['logname'],data['password'],data['expect'])
    def test_02(self):
        '''输入正确的用户名，错误的密码'''
        self.login(data1['logname'],data1['password'],data1['expect'])
if __name__=='__main__':
    discover=unittest.main()
    reportFile = r'd:\TestCase\report\result.html'  # 生成报告路径
    fp = open(reportFile, 'wb')  # 写入的方式打开文件
    runner1 = HTMLTestRunner.HTMLTestRunner(stream=fp, title='123', description='456')
    runner1.run(discover)
    fp.close()

