#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/14 0014
import unittest
import HTMLTestRunner
test_dir=r'E:\testcase'#测试用例文件路径
discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')#匹配路径
reportFile=r'e:\testcase\report\result.html'#生成报告路径
print(reportFile)
fp=open(reportFile,'wb')#写入的方式打开文件
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='第二课堂登录测试报告',description='登录用例的执行情况')
runner.run(discover)
fp.close()
