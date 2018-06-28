#!/usr/bin/env python
# coding=utf-8

# ========================================================
# Summary        :Common
# Author         :Jordan
# Update Date    :2017-12-5
# ========================================================

from Driver import myDriver
import time
import math
import operator
from functools import reduce
from PIL import Image
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from get_log import test_log


class appiumMethod():
    def __init__(self):
        testlog = test_log()
        self.log_folder = testlog.get_log_folder()
        self.pic_folder = testlog.get_test_pic_folder()
        at = myDriver()
        self.driver = at.get_driver()
        self.desired_caps = at.get_desired_caps()

    def wait(self, t):
        self.driver.implicitly_wait(t)

    def get_Size(self):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        return (width, height)

    def swipe_to_up(self, t=800):
        x = self.get_Size()[0]
        y = self.get_Size()[1]
        self.driver.swipe(x * 0.5, y * 0.2, x * 0.5, y * 0.8, t)

    def swipe_to_down(self, t=800):
        x = self.get_Size()[0]
        y = self.get_Size()[1]
        self.driver.swipe(x * 0.5, y * 0.8, x * 0.5, y * 0.2, t)

    def swipe_to_left(self, t=800):
        x = self.get_Size()[0]
        y = self.get_Size()[1]
        self.driver.swipe(x * 0.2, y * 0.5, x * 0.8, y * 0.5, t)

    def swipe_to_right(self, t=800):
        x = self.get_Size()[0]
        y = self.get_Size()[1]
        self.driver.swipe(x * 0.8, y * 0.5, x * 0.2, y * 0.5, t)

    def zoom(self):
        x = self.get_Size()[0]
        y = self.get_Size()[1]
        a1 = TouchAction(
            self.driver).long_press(
            x=x *
            0.1,
            y=y *
            0.83).move_to(
            x=x *
            0.5,
            y=0).release()
        a2 = TouchAction(
            self.driver).long_press(
            x=x *
            0.9,
            y=y *
            0.83).move_to(
            x=-
            x *
            0.5,
            y=0).release()
        ma = MultiAction(self.driver)
        ma.add(a1, a2)
        ma.perform()

    def pinch(self):
        x = self.get_Size()[0]
        y = self.get_Size()[1]
        a1 = TouchAction(
            self.driver).long_press(
            x=x *
            0.6,
            y=y *
            0.83).move_to(
            x=-
            x *
            0.5,
            y=0).release()
        a2 = TouchAction(
            self.driver).long_press(
            x=x *
            0.4,
            y=y *
            0.83).move_to(
            x=x *
            0.5,
            y=0).release()
        ma = MultiAction(self.driver)
        ma.add(a1, a2)
        ma.perform()

    def get_by_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    def get_by_ids(self, id, n=0):
        element = self.driver.find_elements_by_id(id)[n]
        return element

    # android uiautomator2不适用此方法
    # def get_by_name(self,name):
    #    element = self.driver.find_element_by_name(name)
    #    return element

    # def get_by_names(self,name,n = 0):
    #    element = self.driver.find_elements_by_name()[n]
    #    return element

    def get_by_name(self, name):
        element = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("' + name + '")')
        return element

    def get_by_names(self, name, n=0):
        element = self.driver.find_elements_by_android_uiautomator(
            'new UiSelector().text("' + name + '")')[n]
        return element

    def get_by_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def get_by_accessibility_id(self, acc_id):
        element = self.driver.find_element_by_accessibility_id(acc_id)
        return element

    def get_by_accessibility_ids(self, acc_id, n=0):
        element = self.driver.find_elements_by_accessibility_id(acc_id)[n]
        return element

    def get_by_classname(self, classname):
        element = self.driver.find_element_by_class_name(classname)
        return element

    def get_by_classnames(self, classname, n=0):
        element = self.driver.find_elements_by_class_name(classname)[n]
        return element

    def tap(self, x, y):
        self.driver.tap([(x, y)], 300)

    def taps(self, x, y, n=1):
        for i in range(n):
            self.driver.tap([(x, y)], 300)
            time.sleep(0.8)

    def drag_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    def back_and_return(self, t=5):
        self.driver.background_app(t)

    def is_app_installed(self):
        return self.driver.is_app_installed(self.desired_caps['appPackage'])

    def install_app(self):
        self.driver.install_app(self.desired_caps['app'])

    def uninstall_app(self):
        self.driver.remove_app(self.desired_caps['appPackage'])

    def start_activity(self):
        self.driver.start_activity(
            self.desired_caps['appPackage'],
            self.desired_caps['appActivity'])

    def launch_app(self):
        self.driver.launch_app()

    def close_app(self):
        self.driver.close_app()

    def shake(self):
        self.driver.shake()

    def lock_devices(self, t=5):
        self.driver.lock(t)

    def drap_down_notifications(self):
        self.driver.open_notifications()

    def screenshot_to_file(self, caseName):
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        file_path_and_name = self.log_folder + now + caseName + '_screenshot.png'
        self.driver.get_screenshot_as_file(file_path_and_name)

    def pic_comparison(self, x1, y1, x2, y2, shot_pic_name, reference_pic):
        # (x1,y1)(x2,y2)是需要截图的两个坐标比例, reference_pic 是指图片路径，字符串格式
        x = self.get_Size()[0]
        y = self.get_Size()[1]
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        shot_pic = self.pic_folder + 'screenshot_pic\\' + shot_pic_name + now + '.png'
        test_pic = self.pic_folder + 'screenshot_pic\\' + \
            shot_pic_name + now + '_cropfortest.png'
        self.driver.get_screenshot_as_file(shot_pic)
        Image.open(shot_pic).crop(
            (x * x1, y * y1, x * x2, y * y2)).save(test_pic)
        image1 = Image.open(test_pic)
        image2 = Image.open(reference_pic)
        h1 = image1.histogram()
        h2 = image2.histogram()
        result = math.sqrt(reduce(operator.add, list(
            map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h2))
        return result

    def press_keycode(self, keycode):
        self.driver.press_keycode(keycode)

    def long_press_keycode(self, keycode):
        self.driver.long_press_keycode(keycode)

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def network_connection(self):
        return self.driver.network_connection

    def set_network(self, connection_Type):
        self.driver.set_network_connection(connection_Type)
        #  Possible values:
        # Value (Alias)      | Data | Wifi | Airplane Mode
        # -------------------------------------------------
        #0 (None)           | 0    | 0    | 0
        # 1 (Airplane Mode)  | 0    | 0    | 1
        # 2 (Wifi only)      | 0    | 1    | 0
        # 4 (Data only)      | 1    | 0    | 0
        # 6(All network on)  | 1    | 1    | 0
        #

    def contexts(self):
        return self.driver.contexts

    def current_context(self):
        return self.driver.current_context

    def current_activity(self):
        return self.driver.current_activity

    # def page_source(self):
    #   return self.driver.page_source   #为啥调用at.page_source.find() 失败啊？？？

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def reset(self):
        self.driver.reset()

# if __name__ == '__main__':
#    at = appiumMethod()
#    print at.page_source().find(u"略1过·马上体验")
