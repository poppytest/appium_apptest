#!/usr/bin/env python
# coding=utf-8

# ========================================================
# Summary        :Driver
# Author         :Jordan
# Update Date    :2017-12-5
# ========================================================

from appium import webdriver
import time
import get_device_info
import sys

class myDriver():
    def __init__(self):
        device_info = get_device_info.get_devices()

        '''
        # LEPRO3
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'df750fee'
desired_caps['appPackage'] = 'com.gwtsz.gts2'
desired_caps['appActivity'] = 'gw.com.android.ui.WelcomeActivity'
desired_caps['noReset'] = 'True'
# desired_caps['autoLaunch'] = 'False'
desired_caps['newCommandTimeout'] = '6000'  # 超时即关闭应用，appium默认60秒关闭应用；设久一点方便测试。
#desired_caps['unicodeKeyboard'] = 'True'  # 为避免手机当前使用的输入法造成干扰
#desired_caps['resetKeyboard'] = 'True'  # 测试结束恢复原输入法
        self.desired_caps = desired_caps
        '''
        '''
        # NOX Devices
        #adb connect 127.0.0.1:62001
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.gwtsz.gts2'
        desired_caps['appActivity'] = 'gw.com.android.ui.WelcomeActivity'
        desired_caps['noReset'] = 'True'
        #desired_caps['autoLaunch'] = 'False'
        desired_caps['newCommandTimeout'] = '6000'
        #desired_caps['unicodeKeyboard'] = 'True'
        #desired_caps['resetKeyboard'] = 'True'
        #desired_caps['app']='//Users//bear//Downloads//forappium_V161_UAT.apk'
        self.desired_caps = desired_caps
        '''

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['appPackage'] = 'com.gwtsz.gts2'
        desired_caps['appActivity'] = 'gw.com.android.ui.WelcomeActivity'
        desired_caps['noReset'] = 'True'
        #desired_caps['autoLaunch'] = 'False'
        desired_caps['newCommandTimeout'] = '6000'
        #desired_caps['unicodeKeyboard'] = 'True'
        #desired_caps['resetKeyboard'] = 'True'
        #desired_caps['app']='C:\\Users\\Administrator\\Desktop\\forappium_V161_UAT.apk'

        device_num = device_info.get_devices_num()
        if device_num > 1:
            choose_test_device = input('you got more than one devices connected, please choose the number you want to test:')

            desired_caps['platformVersion'] = device_info.get_device_android_version()[(choose_test_device-1)]
            desired_caps['deviceName'] = device_info.get_devices_name()[(choose_test_device-1)]
            self.desired_caps = desired_caps

        elif device_num == 1:
            desired_caps['platformVersion'] = device_info.get_device_android_version()[0]
            desired_caps['deviceName'] = device_info.get_devices_name()[0]
            self.desired_caps = desired_caps

        else:
            print u'Error, please check!'
            sys.exit()


        self.driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)
        #appium -a 127.0.0.1 -p 4723 --session-override  #命令行启动appium server
        #import
        #subprocess.Popen('appium -a 127.0.0.1 -p 4725 --session-override',shell=True)


        time.sleep(1)
        self.driver.reset()
        print "Clear app's data successfully"
        print "The device you test is %s" % (self.desired_caps['deviceName'])
        print "And its screen resolution is %s * %s" % (self.driver.get_window_size()['width'],self.driver.get_window_size()['height'])
        time.sleep(10)

    def get_driver(self):
        return self.driver

    def get_desired_caps(self):
        return self.desired_caps
if __name__ == '__main__':
    aa = myDriver()