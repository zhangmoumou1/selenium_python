# coding=utf-8
import sys
sys.path.append('/home/selenium_python')
import unittest
from public.log import Log
from public import browser
from public.base import Page
from config import globalparam
from selenium import webdriver


class MyTest(unittest.TestCase, Page):

    @classmethod
    def setUpClass(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.driver = browser.select_browser(globalparam.browser)
        # self.driver.implicitly_wait(10)
        Page(self.driver).max_window()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')
