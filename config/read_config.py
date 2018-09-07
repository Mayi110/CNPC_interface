import os
import configparser

public_dir = os.path.dirname(__file__)
config_dir = os.path.join(public_dir,'config.ini')
class readconf:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(config_dir)

    def getmail(self,key):
        value = self.conf.get("Email",key)
        return value
    def gethttp(self,key):
        value = self.conf.get("HTTP",key)
        return value

#t = readconf()
#print(t.getmail("receiver"))




