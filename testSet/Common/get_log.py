#!/usr/bin/env python
# coding=utf-8

# ========================================================
# Summary        :get_device_info
# Author         :Jordan
# Update Date    :2017-12-5
# ========================================================

import os
import time
#from Driver import test_device_info
import subprocess

class test_log():
    def __init__(self):
        self.result_folder = '//Users//bear//Documents//Work//testreport_fold//'
        self.log_folder = '//Users//bear//Documents//Work//testreport_fold//Logs//'
        self.test_pic = '//Users//bear//Documents//Work//testreport_fold//test_pic//'
        self.now = time.strftime("%Y-%m-%d_%H_%M_%S")
        #self.app_folder =

    #def deviceId_folder(self,deviceId):
    #    deviceId_folder = self.result_folder + deviceId + '\\'
    #    return deviceId_folder

    def get_log_folder(self):
        return self.log_folder
    def get_result_folder(self):
        return self.result_folder
    def get_test_pic_folder(self):
        return self.test_pic

    def catch_logcat(self,deviceId):
        logcat_cmd = 'adb -s %s logcat -v time > %s%s_logcat_%s_.log ' % (deviceId, self.log_folder, deviceId, self.now)
        subprocess.Popen(logcat_cmd,shell=True)
        #os.system(start logcat_cmd)
