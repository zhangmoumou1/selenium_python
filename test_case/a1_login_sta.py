import sys
sys.path.append('/home/selenium_python')
import unittest
#import ddt
from public.exceptionscr import Screen
from data.testdata.data_read import Test1
from public.myunit import MyTest
from public import function
from public.base import Page
from test_case.page_obj.a1_loginPage import login
data1 = Test1().a1_data(sheet = "a1_sta")

# @ddt.ddt
# @unittest.skip("跳过此用例")
class loginTest(MyTest,Page):
    """用户密码登录"""

    # @Screen(driver)
    def test_login1(self,expected=True):
        """用户名输入有误"""
        po = login(self.driver)
        po.user_login(username=data1[1]['username'])
        self.assert_equal(po.user_error_hint(actual=data1[1]['result']),expected)
        function.insert_img(self.driver,data1[1]['screenshot_name'])

    def test_login2(self,expected=True):
        """密码输入有误"""
        po = login(self.driver)
        po.user_login(password=data1[2]['password'])
        self.assert_equal(po.pawd_error_hint(actual=data1[2]['result']),expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    #@ddt.data(*data1)
    @unittest.skip("跳过此用例")
    def test_login3(self,expected=True):
        """用户名密码正确,登录成功"""
        po = login(self.driver)
        po.user_login(username=data1[3]['username'], password=data1[3]['password'])
        self.assert_equal(po.user_login_success(actual=data1[3]['result']), expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()


