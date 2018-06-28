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
import subprocess
from get_log import test_log


class myDriver():
    def __init__(self):
        device_info = get_device_info.get_devices()
        get_test_log = test_log()
        server_log_folder = get_test_log.get_log_folder()

        desired_caps = {}
        device_num = device_info.get_devices_num()
        if device_num > 1:
            choose_test_device = input(
                'you got more than one devices connected, please choose the number you want to test:')

            desired_caps['platformVersion'] = device_info.get_device_android_version()[
                (choose_test_device - 1)]
            desired_caps['deviceName'] = device_info.get_devices_name()[
                (choose_test_device - 1)]
            self.desired_caps = desired_caps

        elif device_num == 1:
            choose_test_device = 1
            desired_caps['platformVersion'] = device_info.get_device_android_version()[
                0]
            desired_caps['deviceName'] = device_info.get_devices_name()[0]
            self.desired_caps = desired_caps

        else:
            print u'Error, please check!'
            sys.exit()

        desired_caps['platformName'] = 'Android'
        desired_caps['appPackage'] = 'com.gwtsz.gts2'
        desired_caps['appActivity'] = 'gw.com.android.ui.WelcomeActivity'
        desired_caps['noReset'] = 'True'
        #desired_caps['autoLaunch'] = 'False'
        desired_caps['newCommandTimeout'] = '6000'
        #desired_caps['unicodeKeyboard'] = 'True'
        #desired_caps['resetKeyboard'] = 'True'
        # desired_caps['app']='C:\\Users\\Administrator\\Desktop\\forappium_V164_UAT.apk'

        androidBigVersion = int(desired_caps['platformVersion'].split('.')[0])
        if androidBigVersion >= 5.0:
            print 'Set automationName to UIAutomator2'
            desired_caps['automationName'] = 'UIAutomator2'
        else:
            pass

        self.port = (4725 + choose_test_device - 1)
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        start_server_cmd = 'appium -a 127.0.0.1 -p %d --local-timezone --log-timestamp --session-override > %sServer%d_Port%d_%s.txt' % (
            self.port, server_log_folder, choose_test_device, self.port, now)
        subprocess.Popen(start_server_cmd, shell=True)
        print 'Starting server%d ,and its port is %d' % (
            (choose_test_device), (self.port))
        time.sleep(30)

        server_address = 'http://localhost:%d/wd/hub' % (self.port)

        self.driver = webdriver.Remote(server_address, desired_caps)
        # self.driver.implicitly_wait('10')

        global port
        port = self.port
        global testDeviceId
        testDeviceId = self.desired_caps['deviceName']
        global testDeviceVersion
        testDeviceVersion = self.desired_caps['platformVersion']

        time.sleep(1)
        self.driver.reset()
        print "Clear app's data successfully"
        print "The device you test is %s" % (self.desired_caps['deviceName'])
        print "And its screen resolution is %s * %s" % (
            self.driver.get_window_size()['width'], self.driver.get_window_size()['height'])
        time.sleep(5)

    def get_driver(self):
        return self.driver

    def get_desired_caps(self):
        return self.desired_caps


class test_device_info():
    def get_port(self):
        return port

    def get_deviceId(self):
        return testDeviceId

    def get_deviceVersion(self):
        return testDeviceVersion


if __name__ == '__main__':
    aa = myDriver()
    bb = test_device_info()
    print bb.get_port()
    print bb.get_deviceId()
    print bb.get_deviceVersion()
