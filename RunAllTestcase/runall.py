import sys
sys.path.append("D:\\tomcat-32bit\\apache-tomcat-7.0.90\\webapps\\Jenkins\\workspace\\CNPC_interface")
import unittest
import time
from time import strftime
import os
import HTMLTestRunner
from sendmail import sendmail

def RunAllInterface():
    c_time = strftime('%Y-%m-%d %H-%M-%S',time.localtime())
    file_dir = os.path.dirname(os.path.dirname(__file__))
    resultreport_dir = os.path.join(file_dir,'resultreport/')
    #定义报告的名称格式
    report_name = resultreport_dir + c_time + 'report.html'
    fp = open(report_name,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='CNPC登录接口测试报告',description='用例执行情况')
    #将所有用例加入测试套
    base_dir = os.path.dirname(os.path.dirname(__file__))
    test_dir = os.path.join(base_dir,'testcase/login')
    test_suit = unittest.defaultTestLoader.discover(test_dir,pattern='*.py')
    runner.run(test_suit)
    fp.close()

if __name__ == "__main__":
    RunAllInterface()
    sendmail.send_mail()