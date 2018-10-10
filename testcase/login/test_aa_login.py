import unittest
import os
import sys
sys.path.append("/var/lib/jenkins/workspace/CNPC_interface")
#sys.path.append("../..")
from common.base_api import httpmethod
import requests
import json
import ast
import logging
import logging.handlers
import datetime



class Login(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass


    def test_100_login(self):
        """
        正确登录接口
        :return:
        """
        self.url = httpmethod().set_url(0, 2, 2)
        self.UP = ast.literal_eval(httpmethod().get_username_password(0, 2, 4))
        self.headers = ast.literal_eval(httpmethod().set_headers(0, 1, 3))
        #print(type(self.headers))

        #headers = {'Content-Type':'application/json'}
        t = requests.post(self.url,json=self.UP,headers=self.headers)
        rt = t.text
        #print(rt)
        rt_text = json.loads(rt)
        #print(rt_text)
        #print(rt_text['code'])
        #print(rt_text['msg'])
        #print(rt_text['data']['token'])
        try:
            self.assertIn(rt_text['msg'],'登录成功')
            print("‘正确登录接口’测试成功")
            #logging.warning("此用例测试通过")
            #logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
            #logging.info("tongguo")
            #增加一个headler用于输出日志到控制台
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            s_handler = logging.StreamHandler()
            s_handler.setLevel(logging.INFO)
            logger.addHandler(s_handler)
            #增加一个headler用于输出日志到指定文件
            file_name = os.path.join(os.getcwd(),'log.txt')
            #实例化一个处理器headler
            rf_handler = logging.handlers.TimedRotatingFileHandler(file_name, when='midnight', interval=1,
                                                                   backupCount=7, atTime=datetime.time(0, 0, 0, 0))
            #为处理器设置打印日志的时间格式
            rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            #给日志器logger添加rf_handler处理器
            logger.addHandler(rf_handler)


            logger.debug("this is debug test")
            logger.info("this is info test")
            logger.warning("this is warnning test")
            logger.error("this is error test")
            logger.critical("this is critical test")
        except:
            print("‘正确登录接口’测试失败")
            logging.error("此接口用例测试不通过")

    def test_101_login(self):
        """
        用户名正确，密码错误
        :return:
        """
        self.url = httpmethod().set_url(0, 2, 2)
        self.UP = ast.literal_eval(httpmethod().get_username_password(0, 3, 4))
        self.headers = ast.literal_eval(httpmethod().set_headers(0, 1, 3))
        # print(type(self.headers))

        # headers = {'Content-Type':'application/json'}
        t = requests.post(self.url, json=self.UP, headers=self.headers)
        rt = t.text
        #print(rt)
        rt_text = json.loads(rt)
        #print(rt_text)
        #print(rt_text['code'])
        #print(rt_text['msg'])
        # print(rt_text['data']['token'])
        try:
            self.assertIn(rt_text['msg'], '用户名或密码错误!')
            print("‘异常登录接口’测试成功")
        except:
            print("‘异常登录接口’测试失败")


if __name__ == "__main__":
    unittest.main()