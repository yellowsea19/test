from page.login import loginPage
class activitypage(loginPage):
    all=('xpath','//*[@id="menu10000200"]/span[1]')
    all1=('xpath','//*[@id="menu10000300"]')
    new=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[1]')#点击新增
    abi_name=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[6]/div/div/input')
    scope=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[11]/div/div/div[1]/div/span')#点击报名范围
    scope1=('xpath','//*[@id="ui-select-choices-row-6-0"]/a')#选择报名范围
    sponsor=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[16]/div/div/div[1]/div/ul/li/input')#点击主办方
    sponsor1=('xpath','//*[@id="ui-select-choices-row-2-0"]/div/div')#选择主办方
    abi_type=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[24]/div/div/div[1]/div/span')#点击活动类别
    abi_type1=('xpath','//*[@id="ui-select-choices-row-4-0"]/a/div')#选择活动类别
    img=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[32]/div/sf-decorator[2]/div/button')#点击从图片库选择
    img1=('xpath','/html/body/div[1]/div/div/div[1]/div[6]/div/img')#选择图片
    img_sure=('xpath','/html/body/div[1]/div/div/div[2]/button[2]')#点击确定
    intro=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[34]/div/div/div[1]/div[2]/div')#活动简介
    meaning=('xpath','//*[@id="abiPurpose"]')#活动意义
    target=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[45]/div/label')
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
    save=('xpath','/html/body/div[1]/div/div/div[3]/button[2]')#点击保存
    save1=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')
    def activity(self):
        self.click(self.all)
        self.click(self.all1)



    #
    # def test_audit1(self):
    #     '''活动一审'''
    #     login1.Login(self.driver).login(loginName,passWord)
    #     dj(self.driver,'//*[@id="menu10000200"]/span[1]')#点击活动管理
    #     dj(self.driver,'//*[@id="menu10000300"]')#点击全部活动
    #     dj(self.driver,'//*[@id="ngform"]/div[2]/bootstrap-decorator/div/div[2]/table/tbody/tr[1]/td[3]/div/a')#点击活动
    #     dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[161]/div/sf-decorator[5]/div/button')#点击审核
    #     dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[158]/div/div/div[1]/label[2]/span[1]')#点击同意
    #     dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[161]/div/sf-decorator[3]/div/button')#点击审核
    #     dj(self.driver,'/html/body/div[8]/div/div/div[3]/div/div/button[2]')#点击确定
    #
    # def test_audit2(self):
    #     '''活动二审'''
    #     login1.Login(self.driver).login(loginName,passWord)
    #     dj(self.driver,'//*[@id="menu10000200"]/span[1]')#点击活动管理
    #     dj(self.driver,'//*[@id="menu10000300"]')#点击全部活动
    #     dj(self.driver,'//*[@id="ngform"]/div[2]/bootstrap-decorator/div/div[2]/table/tbody/tr[1]/td[3]/div/a')#点击活动
    #     dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[161]/div/sf-decorator[5]/div/button')#点击二级审核
    #     dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[158]/div/div/div[1]/label[2]/span[1]')#点击同意
    #     dj(self.driver,'//*[@id="editformDiv"]/bootstrap-decorator[161]/div/sf-decorator[3]/div/button')#点击审核
    #     dj(self.driver,'/html/body/div[8]/div/div/div[3]/div/div/button[2]')#点击确定

