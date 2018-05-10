#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018年5月9日

@author: vn0umhp
'''


import smtplib
from email.mime.text import MIMEText
import email.MIMEMultipart
from email.header import Header
import os
import mimetypes

def send_email(receivers= ['1030917233@qq.com'], file_names=[], test_result=0):
    # 第三方 SMTP 服务
    print receivers
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="1030917233@qq.com"    #用户名
    mail_pass="************"   #口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
    sender = '1030917233@qq.com'

    #设置邮件中的测试结果
    resultstr = '失败' if test_result else '通过'

    main_msg = email.MIMEMultipart.MIMEMultipart()
    message = MIMEText('''附件是本次自动化构建的报告，请注意查收 \n\n''', 'plain', 'utf-8')
    main_msg.attach(message)
    result = MIMEText('测试结果： '+resultstr, 'plain', 'utf-8')
    main_msg.attach(result)
    ## 读入文件内容并格式化
    for file_name in file_names:
        data = open(file_name, 'rb')
        ctype,encoding = mimetypes.guess_type(file_name)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype,subtype = ctype.split('/',1)
        file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        email.Encoders.encode_base64(file_msg)#把附件编码

        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
        main_msg.attach(file_msg)

    main_msg['From'] = Header("robot自动发送", 'utf-8')
    reciverstr = ';'.join(receivers)
    main_msg['To'] = Header(reciverstr, 'utf-8')

    subject = 'robotframework测试结果'
    main_msg['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, 465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, main_msg.as_string())
        print "邮件发送成功。"
    except smtplib.SMTPException, e:
        print "Error: 无法发送邮件。错误原因：", e

if __name__ == '__main__':
    send_email(file_names='')
