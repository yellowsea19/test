from selenium import webdriver
from common.config import configPage
url='http://admin2.join-inapp.com/public#/login'
class addhonor(configPage):
    my_center_menu=('xpath','//*[@id="menu10003214"]')
    my_honor_menu=('xpath','//*[@id="menu10002800"]')
    add=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[1]')#点击新增
    honor_type=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[4]/div/div/div[1]/div/span')
    honor_change=('xpath','//*[@id="ui-select-choices-row-1-0"]/a/div')
    honor_stype=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[8]/div/div/div[1]/div/span')
    change_2=('xpath','//*[@id="ui-select-choices-row-2-0"]/a/div')
    zuopinname=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[15]/div/div/input')
    honorname=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[17]/div/div/input')
    starttime=('xpath','//*[@id="uhiDateStart"]')
    starttime1=('xpath','/html/body/div[12]/div[1]/div[2]/table/tbody/tr[4]/td[5]')
    honorjieshao=('xpath','//*[@id="uhiDescription"]')
    save=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[43]/div/sf-decorator[1]/div/input')
    saveConfirmation=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')

    def mycenter(self):
        return  self.click(self.my_center_menu)
    def myhonor(self):
        return  self.click(self.my_honor_menu)
    def add(self):
        return self.click(self.add)
    def honor_type(self):
        self.click(self.honor_type)
        self.click(self.honor_change)
    def honor_stype(self):
        self.click(self.honor_stype)
        self.click(self.change_2)
    def zuopin_name(self,name='autotest'):
        return  self.send_keys(self.zuopinname,name)
    def honor_name(self,name):
        return self.send_keys(self.honorname,name)
    def honor_datestart(self):
        self.click(self.starttime)
        self.click(self.starttime1)
    def honor_jieshao(self):
        self.send_keys()
    def save(self):
        self.click(self.save)
        self.click(self.saveConfirmation)










        #
        # dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[4]/div/div/div[1]/div/span')#点击荣誉类型
        # dj(self.driver,'//*[@id="ui-select-choices-row-1-0"]/a/div')#选择其它类型
        #
        # dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[8]/div/div/div[1]/div/span')#点击荣誉类别
        # time.sleep(1)
        # dj(self.driver,'//*[@id="ui-select-choices-row-2-0"]/a/div')#选择证书
        # time.sleep(1)
        # sr(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[15]/div/div/input','荣誉名称autotest')#作品名称
        # sr(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[17]/div/div/input','dt1')#荣誉名称
        # dj(self.driver,'//*[@id="uhiDateStart"]')#点击获取时间
        # dj(self.driver,'/html/body/div[12]/div[1]/div[2]/table/tbody/tr[4]/td[5]')#点击时间
        # sr(self.driver,'//*[@id="uhiDescription"]','荣誉介绍autotest')#点击荣誉介绍
        # dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[43]/div/sf-decorator[1]/div/input')#点击保存
        # dj(self.driver,'/html/body/div[8]/div/div/div[3]/div/div/button[2]')#确定
