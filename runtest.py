#conding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unittest,time,os,smtplib

#=====================定义发送邮件========================
def send_email(file_new):
    #发送邮件的主题、发件人，收件人，时间的显示
    msg = MIMEMultipart('mixed')
    msg['Subject'] = '自动化测试报告'
    msg['From'] = 'pengl<pengl@servyou.com.cn>'
    msg['To'] = ';'.join(['764442055@qq.com', '18883282817@163.com'])
    #获取邮件正文（以html形式）
    with open(file_new,'rb') as f:
        mail_body=f.read()

    html=MIMEText(mail_body,'html','utf-8')
    msg.attach(html)

    smtp=smtplib.SMTP()
    smtp.connect('mail.servyou.com.cn',25)
    smtp.login('pengl@servyou.com.cn','bp556955')
    smtp.sendmail('pengl@servyou.com.cn',['764442055@qq.com','18883282817@163.com'],msg.as_string())
    smtp.quit()

#=====查找测试报告目录，找到最新生成的测试报告文件============
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getctime(testreport+'\\'+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    test_dir='D:\\GitHub\\autoTestForWeb\\test_case'
    test_report='D:\\GitHub\\autoTestForWeb\\report'

    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

    now=time.strftime('%Y-%m-%d_%H_%M_%S')
    filename=test_report+'\\'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')
    runner.run(discover)
    fp.close()

    new_report=new_report(test_report)
    send_email(new_report)