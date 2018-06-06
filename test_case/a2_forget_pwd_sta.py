import unittest
from public import myunit, function
from public.base import Page
from test_case.page_obj.a2_forget_password import forget
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a2_sta")

# @unittest.skip("跳过此用例")
class PersonalTest(myunit.MyTest,Page):
    """ 忘记密码，找回密码"""

    def test_forget_pwd1(self, expected=True):
        """用户名输入为空"""
        po = forget(self.driver)
        po.forget_pwd1(username=data1[1]['username'])
        self.assert_equal(po.username_error(actual=data1[1]['result']), expected)
        function.insert_img(self.driver, data1[1]['screenshot_name'])

    def test_forget_pwd2(self, expected=True):
        """输入4位数的用户名有误"""
        po = forget(self.driver)
        po.forget_pwd1(username=data1[2]['username'])
        self.assert_equal(po.username_error(actual=data1[2]['result']), expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    def test_forget_pwd3(self, expected=True):
        """输入纯数字的用户名有误"""
        po = forget(self.driver)
        po.forget_pwd1(username=data1[3]['username'])
        self.assert_equal(po.username_error(actual=data1[3]['result']), expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

    def test_forget_pwd4(self, expected=True):
        """当前用户未设置密保"""
        po = forget(self.driver)
        po.forget_pwd1(username=data1[4]['username'])
        self.assert_equal(po.username_error(actual=data1[4]['result']), expected)
        function.insert_img(self.driver, data1[4]['screenshot_name'])

    def test_forget_pwd5(self, expected=True):
        """输入错误次数已超过三次"""
        po = forget(self.driver)
        po.forget_pwd1(username=data1[5]['username'])
        po.forget_pwd2(username=data1[5]['username'])
        self.assert_equal(po.username_error(actual=data1[5]['result']), expected)
        function.insert_img(self.driver, data1[5]['screenshot_name'])

    def test_forget_pwd6(self, expected=True):
        """输入账号正确，进入密保"""
        po = forget(self.driver)
        po.forget_pwd1(username=data1[6]['username'])
        self.assert_equal(po.username_succ(actual=data1[6]['result']), expected)
        function.insert_img(self.driver, data1[6]['screenshot_name'])

    def test_forget_pwd7(self, expected=True):
        """密保答案输入为空"""
        po = forget(self.driver)
        po.forget_pwd1()
        po.answer1(answer=data1[7]['answer'])
        self.assert_equal(po.answer_error1(actual=data1[7]['result']), expected)
        function.insert_img(self.driver, data1[6]['screenshot_name'])

    def test_forget_pwd8(self, expected=True):
        """密保答案失败请求已超过3次机会"""
        po = forget(self.driver)
        po.forget_pwd1()
        po.answer1(answer=data1[8]['answer'])
        self.assert_equal(po.answer_error2(actual=data1[8]['result']), expected)
        function.insert_img(self.driver, data1[8]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()



