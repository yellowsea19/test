#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/14 0014
import unittest
import HTMLTestRunner
test_dir=r'd:\TestCase\testcase'#测试用例文件路径
discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')#匹配路径
runner=unittest.TextTestRunner()#text形式报告
runner.run(discover)#跑用例

reportFile=r'd:\TestCase\report\result.html'#生成报告路径
fp=open(reportFile,'wb')#写入的方式打开文件
runner1=HTMLTestRunner.HTMLTestRunner(stream=fp,title='123',description='456')
runner1.run(discover)
fp.close()

