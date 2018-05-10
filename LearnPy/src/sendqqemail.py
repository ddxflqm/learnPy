#coding: UTF-8
'''
Created on 2018年5月10日

@author: vn0umhp
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from logging import exception

my_sender = "1XXXXX@qq.com"     #发件人邮箱账号
my_pass = ""    #发件人邮箱密码    
my_user = "1XXXXX@qq.com"       #收件人邮箱账号

def mailInfo():
    ret = True
    try:
        msg = MIMEText('填写邮件内容','plain','utf-8')    ##三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        #print (msg)
        msg['from'] = formataddr(["Fromddxflqm",my_sender]) # 发件人昵称，发件人邮箱
        msg['To'] = formataddr(['dd',my_user])  # 收件人昵称，收件人邮箱
        msg['subject']='Python发送邮件测试'   #邮件主题，标题
        
        server = smtplib.SMTP_SSL("smtp.qq.com",465)#发件人邮箱中的SMTP服务器，端口号是465
        server.login(my_sender, my_pass)#括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user], msg.as_string())# 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        
        server.quit()#关闭连接
    except exception:#如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    print ("ret",ret)
    return ret

ret = mailInfo()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
    
        
    
    
    

