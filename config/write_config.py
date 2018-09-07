import os
import configparser


config = configparser.ConfigParser()

try:
    config.add_section("HTTP")
    config.set("HTTP","baseurl","http://qc.petro.devwox.com:8000")
except:
    print("section'HTTP'already exits")

try:
    config.add_section("Email")
    config.set("Email","smtpserver","smtp.163.com")
    config.set("Email","sender","qyt1306@163.com")
    config.set("Email","password","1306qiyuntao")
    config.set("Email","receiver","['qyl1306@163.com','qyt1306@163.com']")
except:
    print("section'Email'already exits")

config.write(open('config.ini','w'))
