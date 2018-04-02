from page.login import loginPage,url

import time,datetime
name_td=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M')
td1=datetime.timedelta(hours=1)
td2=datetime.timedelta(hours=2)
td3=datetime.timedelta(hours=-1)#自定义签到开始时间差
newtd1=td1+datetime.datetime.now()
newtd2=td2+datetime.datetime.now()
newtd3=td3+datetime.datetime.now()
dt1=datetime.datetime.strftime(newtd1,'%Y-%m-%d %H:%M')
dt2=datetime.datetime.strftime(newtd2,'%Y-%m-%d %H:%M')
dt3=datetime.datetime.strftime(newtd3,'%Y-%m-%d %H:%M')
class activitypage(loginPage):

    all=('xpath','//*[@id="menu10000200"]/span[1]')
    all1=('xpath','//*[@id="menu10000300"]')
    new=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[1]')#点击新增
    abi_name=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[6]/div/div/input')
    scope=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[11]/div/div/div[1]/div/span')#点击报名范围
    scope1=('xpath','//*[@id="ui-select-choices-row-6-0"]/a')#选择报名范围
    sponsor=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[16]/div/div/div[1]/div/ul/li/input')#点击主办方
    sponsor1=('xpath','//*[@id="ui-select-choices-row-2-0"]/div/div')#选择主办方
    abi_type=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[24]/div/div/div[1]/div/div/span')#点击活动类别
    abi_type1=('xpath','//*[@id="ui-select-choices-row-4-3"]/a/div')#选择活动类别
    abi_type2=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[24]/div/div/div[1]/div/span')
    abi_type3=('xpath','//*[@id="ui-select-choices-row-4-1"]/a/div')

    target0=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[30]/div/div')
    img=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[32]/div/sf-decorator[2]/div/button')#点击从图片库选择
    img1=('xpath','/html/body/div[1]/div/div/div[1]/div[6]/div/img')#选择图片
    img_sure=('xpath','/html/body/div[1]/div/div/div[2]/button[2]')#点击确定
    intro=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[34]/div/div/div[1]/div[2]/div')#活动简介
    meaning=('xpath','//*[@id="abiPurpose"]')#活动意义
    target1=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[45]/div/label')
    abi_starttime=('xpath','//*[@id="abiStartTime"]')#点击开始时间
    abi_endtime=('xpath','//*[@id="abiEndTime"]')#点击活动结束时间
    sure=('xpath','/html/body/div[13]/div[3]/div/button[1]')
    shichang=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[53]/div/div/div[1]/input')#输入活动时长
    allow=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[64]/div/div/input')#输入报名人数
    sign=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[73]/div/select')
    signnomal=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[73]/div/select/option[2]')#选择普通签到
    signtime=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[76]/div/select')#点击签到开始时间
    signtime1=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[76]/div/select/option[2]')#点击自义定签到时间
    customtime=('xpath','//*[@id="signinStartTime"]')#点击自定义时间
    signbutton=('xpath','/html/body/div[14]/div[3]/div/button[1]')#确定
    map=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[116]/div/div/div[1]/span[2]/sf-decorator/div/button/span')#点击地图
    mapbutton=('xpath','/html/body/div[1]/div/div/div[3]/button[2]')#点击确定
    target2=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[118]/div/div')#定位
    save=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[161]/div/sf-decorator[1]/div/input')#点击保存
    save1=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')
    clickactivity=('xpath','//*[@id="ngform"]/div[2]/bootstrap-decorator/div/div[2]/table/tbody/tr[1]/td[3]/div/a')
    clickaudit1=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[161]/div/sf-decorator[5]/div/button')
    clickagree1=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[158]/div/div/div[1]/label[2]/span[1]')
    clicksure1=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[161]/div/sf-decorator[3]/div/button')
    clicksure2=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')
    clicksure3=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[161]/div/sf-decorator[3]/div/button')
    target3=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[156]/div/div')
    def activity(self,abi_name='autotest'+name_td,intro='autotest',meaning='autotest',dt1=dt1,dt2=dt2,shichang='30',allowmember='100'):
        # time.sleep(3)
        self.click(self.all)#点击活动管理
        self.click(self.all1)#点击全部活动
        self.click(self.new)#点击新增
        self.send_keys(self.abi_name,abi_name)#输入活动名称
        self.click(self.scope) #点击报名范围
        self.click(self.scope1)#选择报名范围
        self.click(self.sponsor)#点击主办方
        self.click(self.sponsor1)#选择主办方
        if url=='http://admin2.join-inapp.com/public#/login':
            self.click(self.abi_type)#选择活动类别
            self.click(self.abi_type1)#选择活动类别
        else:
            self.click(self.abi_type2)
            self.click(self.abi_type3)

        self.js_focus_element(self.target0)#定位
        self.click(self.img)#点击从图片库选择
        self.click(self.img1)#选择图片
        self.click(self.img_sure)#确定
        self.send_keys(self.intro,intro)#输入简介
        self.send_keys(self.meaning,meaning)#活动意义
        self.js_focus_element(self.target1)#元素聚焦
        self.click(self.abi_starttime)#点击活动开始时间
        self.send_keys(self.abi_starttime,'2')#开始时间
        self.send_keys(self.abi_starttime,dt1)
        self.click(self.abi_endtime) #结束时间
        self.send_keys(self.abi_endtime,'2')
        self.send_keys(self.abi_endtime,dt2)
        self.send_keys(self.shichang,shichang)#时长
        self.send_keys(self.allow,allowmember)#输入报名人数
        self.click(self.map)#点击地图
        time.sleep(2)
        self.click(self.mapbutton)#点击确定
        self.js_focus_element(self.target2)
        time.sleep(2)
        self.click(self.save)#点击确定
        time.sleep(1)
        self.click(self.save1)#确认保存


    def audit1(self):
        self.click(self.all)#活动管理
        self.click(self.all1)#全部活动
        self.click(self.clickactivity)#点击活动
        self.click(self.clickaudit1)#点击审核
        self.js_focus_element(self.target3)
        self.click(self.clickagree1)#点击同意审核
        time.sleep(1)
        if url=='http://admin2.join-inapp.com/public#/login':
            self.click(self.clicksure1)#点击确定
        else:
            self.click(self.clicksure3)

        time.sleep(1)
        self.click(self.clicksure2)
    def audit2(self):
        self.click(self.all)#活动管理
        self.click(self.all1)#全部活动
        self.click(self.clickactivity)#点击活动
        self.click(self.clickaudit1)#点击审核
        self.js_focus_element(self.target3)
        self.click(self.clickagree1)#点击同意审核
        time.sleep(1)
        if url=='http://admin2.join-inapp.com/public#/login':
            self.click(self.clicksure1)#点击确定
        else:
            self.click(self.clicksure3)

        time.sleep(1)
        self.click(self.clicksure2)


