#!/usr/bin/env python
# coding=utf-8

# ========================================================
# Summary        :testsuite
# Author         :Jordan
# Update Date    :2017-12-5
# ========================================================

import testcase
import sys


class DefineTestSuite():
    def __init__(self):
        self.testcase = testcase.DefineTestCase
        self.testunit = testcase.unittest.TestSuite()

        #self.n = raw_input('Please input the test times you want to test:')
        self.n = str(1)
        n = int(self.n)
        if self.n.isdigit():

            if n == 1:
                print "######## %d time to run, please wait! ########" % (n)
            elif n > 0:
                print "######## %d times to run, please wait! ########" % (n)
            else:
                print "Please input a positive integer!"
                sys.exit()
        else:
            print "Please input a positive integer!"
            sys.exit()

        for i in range(n):
            self.testunit.addTests(
                testcase.unittest.TestLoader().loadTestsFromTestCase(
                    self.testcase))

    def testunit(self):
        return self.testunit

    def runtimes(self):
        return int(self.n)
