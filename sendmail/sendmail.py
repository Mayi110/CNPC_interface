import sys
sys.path.append("/var/lib/jenkins/workspace/CNPC_interface")
sys.path.append("D:\\tomcat-32bit\\apache-tomcat-7.0.90\\webapps\\Jenkins\\workspace\\CNPC_interface")
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common import FindNewReport

def send_mail():
    smtpserver = 'smtp.163.com'
    sender = 'qyl1306@163.com'
    password = '1306qiyunlong'
    receiver = ['qyt1306@163.com','qiyunlong@bmsoft.com.cn']

    subject = '接口自动化测试报告'

    fp = open(FindNewReport.new_report(),'rb')
    sendfile = fp.read()
    fp.close()

    msg = MIMEText(sendfile,_subtype='html',_charset='utf-8')
    msg['subject'] = Header(subject,'utf-8')
    msg['from'] = sender
    msg['to'] = ";".join(receiver)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,msg.as_string())
    except:
        print("邮件发送失败")
    else:
        print("邮件发送成功")
    finally:
        smtp.quit()