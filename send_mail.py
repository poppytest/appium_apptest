#!/usr/bin/env python
# coding=utf-8

# ========================================================
# Summary        :sendmail
# Author         :Jordan
# Update Date    :2017-12-5
# ========================================================

import yagmail
def sendtestmail(attachmentAddress = None):
    #发件人信息
    yag = yagmail.SMTP(user='autotestbyjordan@gmail.com', password='!@c20171111', host='smtp.gmail.com')

    #收件人
    receiver = ['martin.liu@gwtsz.net', 'jordan.wang@gwtsz.net']

    #抄送收件人
    cc = ['245302644@qq.com']

    #邮件主题
    body = ['AutoTestReport, please check the attachment!']

    # 邮箱正文
    contents = [u'自动化测试完毕，请查看附件报告，有疑问请联系Jordan...','Thanks!']


    # 发送邮件
    yag.send(receiver, body, contents, attachmentAddress, cc)
