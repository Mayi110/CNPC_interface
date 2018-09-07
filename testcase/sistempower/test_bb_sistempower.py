import unittest
from common.base_api import httpmethod
import json
import requests


class addsistempower(unittest.TestCase):
    def setUp(self):
        self.url = httpmethod().set_url(0,1,2)
        self.headers = httpmethod().set_headers(0,1,3)
        self.params = httpmethod().set_params(0,1,4)
    def test_200_addpower(self):
        """
        增加系统权限接口
        :return:
        """
        s = requests.session()
        r = s.post(self.url,data=self.params)
        print(r)
        result = r.text
        result_text = json.loads(result)
        print(result_text)

if __name__ == "__main__":
    unittest.main