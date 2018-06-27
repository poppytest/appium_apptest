#!/usr/bin/env python
# coding=utf-8

# ========================================================
# Summary        :runtest
# Author         :Jordan
# Update Date    :2017-12-5
# ========================================================

import os
import HTMLTestRunner
import time
import sys
from testSet.testsuite import DefineTestSuite
from testSet.Common.Driver import test_device_info
from testSet.Common.get_log import test_log
from send_mail import sendtestmail
#from multiprocessing import Process
import subprocess

if __name__ == '__main__':
    suite = DefineTestSuite()
    testunit = suite.testunit
    testLog = test_log()
    deviceInfo = test_device_info()
    port = deviceInfo.get_port()
    deviceId = deviceInfo.get_deviceId()
    deviceVersion=deviceInfo.get_deviceVersion()

    result_folder = testLog.get_result_folder()
    log_folder = testLog.get_log_folder()
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    time.sleep(1)

    #p_logcat = Process(target=testLog.catch_logcat(deviceId))
    #p_logcat.daemon = True
    #p_logcat.start()   多进程导致主进程参数没了？得重新初始化？

    #t_logcat= threading.Thread(target=testLog.catch_logcat(deviceId))
    #t_logcat.setDaemon(True)
    #t_logcat.start()
    testLog.catch_logcat(deviceId)

    filename = '%s%s_V%s_Port%s__%s_TestResult.html' % (result_folder, deviceId, deviceVersion, str(port), now)
    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'%s共测试%d轮的测试报告' % (deviceId,suite.runtimes()),
        description=u'用例的执行情况'
    )

    runner.run(testunit)
    time.sleep(1)
    fp.close()
    #toKillServer_cmd = 'for /f "tokens=5" ' + '%a in ' + "('netstat -aon^|findstr 127.0.0.1:%s^|findstr LISTENING')" % (port) + 'do @taskkill /F /PID %a'
    toKillServer_cmd = 'kill -9 $(lsof -t -i:%d)' % (port)
    os.system(toKillServer_cmd)   #杀掉appium server
    print u'Close appium server successfully!'
    #sendtestmail(filename)
    #print u'Report发送成功,请查收'

    print u'Test End!'
    sys.exit()  # 退出进程



