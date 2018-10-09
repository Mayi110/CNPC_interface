import requests
import sys
sys.path.append("D:\\tomcat-32bit\\apache-tomcat-7.0.90\\webapps\\Jenkins\\workspace\\CNPC_interface")
from common import read_excel
from config import read_config

readingconf = read_config.readconf()
#read_excel.readxlrd(0,1,2)
class httpmethod:
    def __init__(self):
        self.host = readingconf.gethttp("baseurl")
#        self.headers = read_excel.readxlrd(0,1,3)

    def get_username_password(self,m,n,t):
        self.username_password = read_excel.readxlrd(m,n,t)
        return self.username_password
    def set_url(self,m,n,t):
        self.url = self.host + read_excel.readxlrd(m,n,t)
        return self.url
    def set_headers(self,m,n,t):
        self.headers = read_excel.readxlrd(m,n,t)
        return self.headers
    def set_params(self,m,n,t):
        self.params = read_excel.readxlrd(m,n,t)
        return self.params
    def set_data(self,m,n,t):
        self.data = read_excel.readxlrd(m,n,t)


#print(httpmethod().set_url(0,1,2))
