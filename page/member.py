from common.config import configPage
import time
from page import loginpage
class member(loginpage.loginPage):
    oclikc=('xpath','//*[@id="menu10000146"]')#组织机构管理
    renyuan=('xpath','//*[@id="menu10000154"]')#人员信息管理
    new=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[1]')#新增
    name=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[3]/div/div/input')#姓名
    loginname=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[5]/div/div/input')#登录名
    paw=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[6]/div/div/input')#密码
    paw1=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[7]/div/div/input')#密码确认
    org=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[25]/div/div/div[1]/span')#隶属机构
    keda=('xpath','/html/body/div[1]/div/div/div[2]/div/joinin-group-select/div/ul/li/a')#选择科大
    sure=('xpath','/html/body/div[1]/div/div/div[3]/button[3]')#确定
    gradecode=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[32]/div/div/input')#学号
    role=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[96]/div/div/div[1]/ul/li/input')
    role1=('xpath','//*[@id="ui-select-choices-row-2-6"]/div')#选择角色
    save=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[101]/div/sf-decorator[1]/div/input')
    save1=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')#保存

    del_change=('xpath','//*[@id="ngform"]/div[2]/bootstrap-decorator/div/div[2]/table/tbody/tr[1]/td[1]/div/label')
    delcl=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[4]')
    delsure=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')
    rubbish=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[6]' )
    del_change1=('xpath','//*[@id="ngform"]/div[2]/bootstrap-decorator/div/div[2]/table/tbody/tr[1]/td[1]/div/label')
    delover=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[2]')
    delsure1=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')


    def addmember(self,name='autotest',loginname='19900000001',psw='11111111',gradecode='aututest001'):
        self.click(self.oclikc)#点击组织机构管理
        self.click(self.renyuan)#点击人员信息管理
        self.click(self.new)#点击新增
        time.sleep(3)
        self.send_keys(self.name,name)#输入姓名
        self.send_keys(self.loginname,loginname)#输入用户名手机号码
        self.send_keys(self.paw,psw)#输入密码
        self.send_keys(self.paw1,psw)#输入密码确认
        self.click(self.org)#点击隶属机构
        self.click(self.keda)#选择科大
        self.click(self.sure)#点击确定
        self.send_keys(self.gradecode,gradecode)#输入学号
        time.sleep(2)
        self.click(self.role)#点击角色
        time.sleep(2)
        self.click(self.role1)#选择角色
        self.click(self.save)#点击保存
        self.click(self.save1)#保存确认
    def delmember(self):
        self.click(self.oclikc)#点击组织机构管理
        self.click(self.renyuan)#点击人员信息管理
        self.click(self.del_change)#选中删除人员
        self.click(self.delcl)#点击删除
        self.click(self.delsure)#确认删除
        time.sleep(2)
        self.click(self.rubbish)#点击回收站
        self.click(self.del_change)#选择数据
        self.click(self.del_change)#选择数据
        time.sleep(2)
        self.click(self.delover)#点击彻底删除
        time.sleep(2)
        self.click(self.delsure1)#点击删除确认





