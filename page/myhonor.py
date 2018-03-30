from selenium import webdriver
from common.config import configPage,url
from page import login

class addhonor(login.loginPage):
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
    changhonor=('xpath','//*[@id="ngform"]/div[2]/bootstrap-decorator/div/div[2]/table/tbody/tr[1]/td[1]/div/label')
    changdel=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[3]')
    delsure=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')
    def mycenter(self):
        return  self.click(self.my_center_menu)
    def myhonor(self):
        return  self.click(self.my_honor_menu)
    def ad(self):
        return self.click(self.add)
    def honor_type1(self):
        return self.click(self.honor_type)
    def honor_type2(self):
        return self.click(self.honor_change)
    def honor_stype1(self):
        return self.click(self.honor_stype)
    def honor_stype2(self):
        return self.click(self.change_2)
    def zuopin_name(self,text):
        return  self.send_keys(self.zuopinname,text)
    def honor_name(self,text):
        return self.send_keys(self.honorname,text)
    def honor_datestart1(self):
        return self.click(self.starttime)
    def honor_datestart2(self):
        self.click(self.starttime1)
    def honor_jieshao(self,text):
        self.send_keys(self.honorjieshao,text)
    def save1(self):
        return self.click(self.save)
    def save2(self):
        return self.click(self.saveConfirmation)

    def newhonor(self,zuopinname='autotest',honorname='autotest',jieshao='autotest'):
        self.mycenter()#点击个人中心
        self.myhonor()
        self.ad()
        self.honor_type1()
        self.honor_type2()
        self.honor_stype1()
        self.honor_stype2()
        self.zuopin_name(zuopinname)
        self.honor_name(honorname)
        self.honor_datestart1()
        self.honor_datestart2()
        self.honor_jieshao(jieshao)
        self.save1()
        self.save2()
    def delhonor(self):
        self.mycenter()#点击个人中心
        self.myhonor()
        self.click(self.changhonor)
        self.click(self.changdel)
        self.click(self.delsure)



if __name__=='__main__':
    driver=addhonor()
    driver.login()
    driver.mycenter()
    driver.myhonor()
    driver.ad()
    driver.honor_type1()
    driver.honor_type2()
    driver.honor_stype1()
    driver.honor_stype2()
    driver.zuopin_name()
    driver.honor_name()
    driver.honor_datestart1()
    driver.honor_datestart2()
    driver.honor_jieshao()
    driver.save1()
    driver.save2()























