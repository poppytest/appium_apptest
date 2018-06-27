#!/usr/bin/env python
# coding=utf-8

# ========================================================
# Summary        :testcase
# Author         :Jordan
# Update Date    :2017-12-5
# ========================================================

import time
import unittest
import random
from selenium.common.exceptions import NoSuchElementException
from Common.Common import appiumMethod


class startdriver:
    def __init__(self):
        self.at = appiumMethod()

    def get_driver(self):
        return self.at


class DefineTestCase(unittest.TestCase):
    global toinitdriver
    #global
    toinitdriver = startdriver()

    def setUp(self):
        self.at = toinitdriver.get_driver()
        print "Start test"
        self.watcherstate = True
        while self.watcherstate == True:
            try:
                if (self.at.driver.page_source.find(u'权限申请')) != -1 or (self.at.driver.page_source.find('com.android.packageinstaller:id/permission_message')) != -1 or (self.at.driver.page_source.find('android:id/alertTitle')) != -1 or (self.at.driver.page_source.find('com.lbe.security.miui:id/permission_message')) != -1 or (self.at.driver.page_source.find('miui:id/customPanel')) != -1 or (self.at.driver.page_source.find('oppo:id/permission_prompt')) != -1 or (self.at.driver.page_source.find(u'com.gwtsz.gts2:id/ads_imageview')) != -1 :
                    #权限申请：乐视手机；谷歌手机；魅族flyme手机；华为手机；MIUI8.5; oppo color OS V3.0；
                    #优惠券活动弹框；
                    try:
                        self.at.get_by_id('oppo:id/remember_cb').click()
                        time.sleep(1)
                        self.at.get_by_name('允许并继续').click()
                        time.sleep(2)
                    except:
                        pass
                    try:
                        # self.at.get_by_xpath("//android.widget.TextView[contains(@text, '允许')]").click()
                        # self.at.get_by_id("com.android.packageinstaller:id/permission_allow_button").click()
                        self.at.get_by_name('允许').click()
                        time.sleep(2)
                    except:
                        pass
                    try:
                        self.at.get_by_name('始终允许').click()
                        time.sleep(2)
                    except:
                        pass
                    try:
                        self.at.get_by_id('com.gwtsz.gts2:id/btn_cancel').click()
                        time.sleep(2)
                    except:
                        pass
                else:
                    self.watcherstate = False
            except:
                pass

    def tearDown(self):
        print "End for this case"

    def test_case001_open_app(self):
        try:
            if (self.at.driver.page_source.find(self.at.desired_caps['appPackage'])) != -1:
                print u"打开app成功"
            else:
                print u"打开app失败，请检查"
                self.assertTrue(0)
        except Exception:
            print u"Error,open app failed"
            self.at.screenshot_to_file('open_app')
            self.assertTrue(0)

    def test_case002_guide_page(self):
        try:
            self.at.swipe_to_right(500)
            time.sleep(2)
            print u"右滑"
            pic_compare_result = self.at.pic_comparison(0.2664, 0.9083, 0.7354, 0.9542, 'guidepage', '//Users//bear//Documents//Work//testreport_fold//test_pic//refer_pic//skip_guide_refer_pic.png')
            #self.at.get_by_xpath("//android.widget.TextView[contains(@text, '略过·马上体验')]").click()
            self.at.get_by_id("com.gwtsz.gts2:id/startbtn").click()
            print u"有向导页面，跳过"
            time.sleep(5)
        except NoSuchElementException:
                print u"无向导页面，直接进入首页"
        except Exception:
            self.at.screenshot_to_file('guide_page_fail')
            print u"Error,guide page failed"
            self.assertTrue(0)
        print u'截图对比后结果为' + str(pic_compare_result)
        self.assertLessEqual(pic_compare_result, 1000, u'The case fails because its ratio exceeds expectations')
        # 坐标截图，不同分辨率手机导致截出效果不理想，此处暂时对比度为1000


    def test_case003_close_update(self):
        try:
            self.at.get_by_name('以后再说').click()
            print u"关闭升级提示成功"
            time.sleep(5)

        except NoSuchElementException:
            print u"无升级提示"
        except Exception:
            print u"Error, close ad failed"
            self.assertTrue(0)

    def test_case004_close_ad(self):
        try:
            self.at.get_by_id("com.gwtsz.gts2:id/btn_cancel").click()
            print u"关闭弹框广告成功"
            time.sleep(5)

        except NoSuchElementException:
                print u"无弹框广告"
        except Exception:
            self.at.screenshot_to_file('close_ad')
            print u"Error, close ad failed"
            self.assertTrue(0)

    def test_case005_enter_MyPage(self):
        try:
            self.at.get_by_xpath("//android.widget.TextView[@text='我']").click()
            print u"打开'我'页面成功"
            time.sleep(5)
        except Exception:
            self.at.screenshot_to_file('enter_MyPage')
            print u"Error, open My Page failed"
            self.assertTrue(0)


    def test_case006_enter_LoginPage(self):
        try:
            self.at.get_by_id("com.gwtsz.gts2:id/login_btn").click()
            print u"进入登陆页面"
            time.sleep(5)
        except Exception:
            self.at.screenshot_to_file('enter_LoginPage')
            print u"Error, open Login Page failed"
            self.assertTrue(0)

    def test_case007_try_login_byPhone(self):
        try:
            #print u"登陆账户为：18044441234/a123456（PRD场账户）"
            print u"登陆账户为：13811113333/ab123456（uat场账户）"
            self.at.get_by_id("com.gwtsz.gts2:id/loginnameEditText").click()
            self.at.get_by_id("com.gwtsz.gts2:id/loginnameEditText").send_keys("13811113333")
            time.sleep(2)
            self.at.get_by_id("com.gwtsz.gts2:id/password").click()
            self.at.get_by_id("com.gwtsz.gts2:id/password").send_keys("ab123456")
            time.sleep(2)
            self.at.get_by_id("com.gwtsz.gts2:id/sign_in_button").click()
            time.sleep(21)
        except Exception:
            self.at.screenshot_to_file('try_login_byPhone')
            print u"Error,try login by phoneNum failed"
            self.assertTrue(0)

    def test_case008_check_login_state(self):
        try:
            if (self.at.driver.page_source.find(u"解盘"))!= -1 or (self.at.driver.page_source.find(u"解盤"))!= -1:
                print u"登录成功"
            else:
                print u"登录失败，进行检查:"
                if (self.at.driver.page_source.find(u"服务器无响应，请稍后再试(1201)"))!= -1:
                    print u"服务器无响应，请稍后再试(1201)"
                elif (self.at.driver.page_source.find(u"服务器无响应，请稍后再试(1202)"))!= -1:
                    print u"服务器无响应，请稍后再试(1202)"
                elif (self.at.driver.page_source.find(u"服务器无响应，请稍后再试(1205)"))!= -1:
                    print u"服务器无响应，请稍后再试(1205)"
                elif (self.at.driver.page_source.find(u"密码错误(1)"))!= -1:
                    print u"密码错误(1)"
                elif (self.at.driver.page_source.find(u"请输入正确用户账号(13)"))!= -1:
                    print u"请输入正确用户账号(13)"
                elif (self.at.driver.page_source.find(u"密码错误(1)"))!= -1:
                    print u"密码错误(1)"
                elif (self.at.driver.page_source.find(u"请选择您要登录的账户类型（若仍失败，请尝试用交易账号登录）"))!= -1:
                    print u"真实模拟账户接口异常，选择真实或模拟账户直接登录，此处选择真实账户登录"
                    self.at.get_by_id("com.gwtsz.gts2:id/action_btn_neg").click()
                    time.sleep(20)
                    DefineTestCase.test_case008_check_login_state(self)
                else:
                    self.at.screenshot_to_file('check_login_state')
                    print u"some error happened, please check"
                    self.assertTrue(0)

        except Exception:
            self.at.screenshot_to_file('check_login_state')
            print u"Error,try login by phoneNum failed"
            self.assertTrue(0)
        # finally:
        #     self.at.reset()
        #     print "Clear app's data and exit"
        #     time.sleep(5)

    def test_case009_enter_market_page(self):
        try:
            self.at.get_by_name(u'行情').click()
            self.at.get_by_name(u'行情').click()   #跳过向导
            self.at.get_by_name(u'行情').click()   #跳过向导
        except Exception:
            self.at.screenshot_to_file('enter_market_page')
            print u'Error,try enter_market_page failed'
            self.assertTrue(0)


    def test_case010_enter_chart_page(self,product_num = 0):
        global global_product_num
        global_product_num = product_num
        try:
            self.at.get_by_ids('com.gwtsz.gts2:id/ll_product_item', global_product_num).click()
            time.sleep(10)
        except Exception:
            self.at.screenshot_to_file('enter_chart_page')
            print u"Error,try enter_chart_page failed"
            self.assertTrue(0)

    #@unittest.skip(u"强制跳过图表操作")
    def test_case011_chart_action(self):
        try:
            self.at.get_by_name(u'日K').click()
            print u'切换日K'
            time.sleep(5)
            self.at.swipe_to_left()
            time.sleep(1)
            self.at.swipe_to_left()
            time.sleep(5)
            self.at.swipe_to_right()
            print u'滑动K线'
            self.at.zoom()
            self.at.zoom()
            time.sleep(5)
            self.at.pinch()
            time.sleep(5)
            print u'缩放K线'
            time.sleep(1)
            self.at.swipe_to_left()
            self.at.get_by_id('com.gwtsz.gts2:id/arrow_view').click()
            print u'回到当前K线'
            time.sleep(1)
            self.at.get_by_id('com.gwtsz.gts2:id/main_btn_layout').click()
            time.sleep(2)
            self.at.get_by_name(u'PBX').click()
            time.sleep(1)
            self.at.get_by_id('com.gwtsz.gts2:id/main_btn_layout').click()
            time.sleep(2)
            self.at.get_by_name(u'RSI').click()
            time.sleep(1)
            if self.at.driver.page_source.find(u"PBX") == -1 or self.at.driver.page_source.find(u"RSI") == -1:
                print u'切换指标失败，请检查'
                self.at.screenshot_to_file('chart_action')
                self.assertTrue(0)
            else:
                print u'切换指标成功'
        except Exception:
            self.at.screenshot_to_file('chart_action')
            print u"Error,try chart_action failed"
            self.assertTrue(0)

    def test_case012_enter_trade_page(self):
        global global_product_num
        try:
            current_product = self.at.get_by_id('com.gwtsz.gts2:id/app_title').text.replace('\n', '')
            self.at.get_by_id('com.gwtsz.gts2:id/buy_price_layout').click()
            time.sleep(1)
            if self.at.driver.page_source.find(u"市价")!= -1:
                print u'进入当前产品（%s）的下单交易页面' % (current_product)
            elif self.at.driver.page_source.find(u"登录") != -1:
                print u'case008中未登录成功，导致无法进入交易页面'
                self.assertTrue(0)
            elif self.at.driver.page_source.find(u"当前产品只可进行平仓操作，如有疑问，请联系相关客服人员")!= -1:
                print u'当前产品(%s)只可进行平仓操作，无法进入下单页面' % (current_product)
                self.at.get_by_name(u'确定').click()
                self.at.get_by_id('com.gwtsz.gts2:id/title_left_btn').click()
                time.sleep(1)
                global_product_num = global_product_num + 1
                DefineTestCase.test_case010_enter_chart_page(self, global_product_num)
                DefineTestCase.test_case012_enter_trade_page(self)
            elif self.at.driver.page_source.find(u"参考行情，不提供交易服务") != -1:
                print u'当前产品(%s)是参考行情，无法进入下单页面' % (current_product)
                self.at.get_by_name(u'确定').click()
                self.at.get_by_id('com.gwtsz.gts2:id/title_left_btn').click()
                time.sleep(1)
                global_product_num = global_product_num + 1
                DefineTestCase.test_case010_enter_chart_page(self, global_product_num)
                DefineTestCase.test_case012_enter_trade_page(self)
            elif self.at.driver.page_source.find(u"产品已过期，不可交易") != -1:
                print u'当前产品(%s)已过期，无法进入下单页面' % (current_product)
                self.at.get_by_name(u'确定').click()
                self.at.get_by_id('com.gwtsz.gts2:id/title_left_btn').click()
                time.sleep(1)
                global_product_num = global_product_num + 1
                DefineTestCase.test_case010_enter_chart_page(self, global_product_num)
                DefineTestCase.test_case012_enter_trade_page(self)
            elif self.at.driver.page_source.find(u"与服务器断开连接,请稍后交易") != -1:
                print u'进入下单页面时，与服务器断开连接,需稍后交易'
                time.sleep(5)
                self.at.get_by_id('com.gwtsz.gts2:id/action_btn_pos').click()
                time.sleep(1)
                DefineTestCase.test_case012_enter_trade_page(self)

        except Exception:
            self.at.screenshot_to_file('enter_trade_page')
            print u"Error,try enter_trade_page failed"
            self.assertTrue(0)

    def test_case013_do_trade(self, input_lot_multiplier = 1):
        try:
            lot_range_info = self.at.get_by_ids('com.gwtsz.gts2:id/title_view_range', 1).text.replace('[', '_').replace(']', '_').replace('-', '_').replace(u'手', '_')
            trade_lot_range = lot_range_info.split('_')
            input_lot = round(random.uniform(float(trade_lot_range[1]), float(trade_lot_range[3])), 1) * input_lot_multiplier
            self.at.get_by_ids('com.gwtsz.gts2:id/number_input', 1).click()
            self.at.get_by_ids('com.gwtsz.gts2:id/number_input', 1).clear()
            self.at.get_by_ids('com.gwtsz.gts2:id/number_input', 1).send_keys(str(input_lot))
            print u'尝试下单'+str(input_lot)+u'手，若合适，则进行下一步'
            if self.at.driver.page_source.find("com.gwtsz.gts2:id/morder_alarm_title") == -1:
                self.at.get_by_id('com.gwtsz.gts2:id/btn_custom_confirm').click()
                time.sleep(61) #网络慢时会延时60s才弹提示框
            else:
                print u'输入错误，继续改手数'
                DefineTestCase.test_case013_do_trade(self)
        except Exception:
            self.at.screenshot_to_file('do_trade')
            print u"Error,try trade failed"
            self.assertTrue(0)

    def test_case014_check_trade_result(self):
        try:
            if self.at.driver.page_source.find(u"市价开仓成功")!= -1:
                print u'市价开仓成功：'+ self.at.get_by_id('com.gwtsz.gts2:id/res_status_content2').text +self.at.get_by_id('com.gwtsz.gts2:id/res_status_content3').text
            elif self.at.driver.page_source.find(u"市价开仓失败")!= -1:
                print u'市价开仓失败：'+ self.at.get_by_id('com.gwtsz.gts2:id/res_status_pro').text +self.at.get_by_id('com.gwtsz.gts2:id/res_status_content').text
                print u'返回重新下单'
                if self.at.driver.page_source.find(u"保证金不足，为保证不影响您的交易，请及时补充资金(39)")!= -1:
                    self.at.get_by_id('com.gwtsz.gts2:id/btn_custom_left').click()
                    DefineTestCase.test_case013_do_trade(self, 0.1)
                    DefineTestCase.test_case014_check_trade_result(self)
                else:
                    self.at.get_by_id('com.gwtsz.gts2:id/btn_custom_left').click()
                    DefineTestCase.test_case013_do_trade(self)
                    DefineTestCase.test_case014_check_trade_result(self)
            elif self.at.driver.page_source.find(u"与服务器断开连接,请稍后交易")!= -1:
                print u'与服务器断开连接，需要重新尝试'
                self.at.get_by_id('com.gwtsz.gts2:id/action_btn_pos').click()
                time.sleep(5)
                self.at.get_by_id('com.gwtsz.gts2:id/btn_custom_confirm').click()
                time.sleep(61)
                DefineTestCase.test_case014_check_trade_result(self)
            elif self.at.driver.page_source.find(u"提示")!= -1 :
                print u'提交订单时网络状态不好，订单可能成交也可能未成交，故执行重新下单'
                self.at.get_by_id('com.gwtsz.gts2:id/action_btn_pos').click()
                time.sleep(5)
                DefineTestCase.test_case012_enter_trade_page(self)
                DefineTestCase.test_case013_do_trade(self)
                DefineTestCase.test_case014_check_trade_result(self)
        except Exception:
            self.at.screenshot_to_file('check_trade_result')
            print u"Error,try check_trade_result failed"
            self.assertTrue(0)

'''
if __name__ == '__main__':

    #DefineTestCase.startdriver()
    runner = unittest.TextTestRunner()
    testunit = unittest.TestSuite()
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(DefineTestCase))
    runner.run(testunit)

#aaaa = DefineTestCase()
'''