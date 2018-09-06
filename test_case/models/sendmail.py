#coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#邮件发送人和接受人
sender='pengl@servyou.com.cn'
receiver=['764442055@qq.com','18883282817@163.com']
#构造邮件正文及附件
def email():
    #邮件主题，收件人，发送人时间的展示
    msg=MIMEMultipart('mixed')
    msg['Subject']='自动发送邮件学习'
    msg['From']=sender
    msg['To']=';'.join(receiver)

    #邮件正文
    mail_plain_txt='hi!\n 邮件正文的编写'
    mail_plain=MIMEText(mail_plain_txt,'plain','utf-8')
    msg.attach(mail_plain)
    return msg

#发送邮件
def send_email(msg):
    smtp=smtplib.SMTP()
    smtp.connect('mail.servyou.com.cn',25)
    smtp.login(sender,'bp556955')
    smtp.sendmail(sender,receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    msg=email()
    send_email(msg)