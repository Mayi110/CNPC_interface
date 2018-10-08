import unittest
import sys
sys.path.append("../../")
from common.base_api import httpmethod
import requests
import json
import ast



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
        except:
            print("‘正确登录接口’测试失败")

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
    unittest.main
