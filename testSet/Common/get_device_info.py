#!/usr/bin/env python
# coding=utf-8

# ========================================================
# Summary        :get_device_info
# Author         :Jordan
# Update Date    :2017-12-5
# ========================================================

import os
#import subprocess
import sys
import re


class get_devices():
    def __init__(self):
        try:
            #deviceInfo = subprocess.check_output('adb devices').split("\r\n")
            readDeviceId = list(os.popen('adb devices').readlines())
            if readDeviceId[1] == '\n':
                print u"No devices connected!"
                self.deviceName = None
                self.deviceNum = 0
                self.deviceVersion = None
                sys.exit()

            elif len(readDeviceId) == 3:
                deviceId = re.findall(r'\S*', readDeviceId[1])[0]
                print u"The connected device is %s" % (deviceId)
                self.deviceName = []
                self.deviceName.append(deviceId)
                self.deviceNum = 1

                deviceAndroidVersion = list(
                    os.popen("adb shell getprop ro.build.version.release").readlines())
                self.deviceVersion = []
                self.deviceVersion.append(re.findall(
                    r'\S*', deviceAndroidVersion[0])[0])

            else:
                self.deviceNum = len(readDeviceId) - 2
                print u"%d devices connected:" % (self.deviceNum)
                self.deviceName = []
                for devices in readDeviceId[1:(self.deviceNum + 1)]:
                    deviceId = re.findall(r'\S*', devices)[0]
                    self.deviceName.append(deviceId)
                    print deviceId

                self.deviceVersion = []
                for i in range(self.deviceNum):
                    deviceAndroidVersion = list(
                        os.popen(
                            "adb -s %s shell getprop ro.build.version.release" %
                            (self.deviceName[i])).readlines())
                    deviceVersion = re.findall(
                        r'\S*', deviceAndroidVersion[0])[0]
                    self.deviceVersion.append(deviceVersion)

        except Exception:
            print u"adb error,please check!"
            sys.exit()

    def get_devices_name(self):
        return self.deviceName

    def get_devices_num(self):
        return self.deviceNum

    def get_device_android_version(self):
        return self.deviceVersion
