from public.base import Page
from config import globalparam
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a2_sta")

class forget(Page):
    """
    Forget password page
    """
    url = "/www/goFindPwd"
    #定位器
    forget_name_loc = ("id", "username")
    forget_submit_loc = ("css selector", "img[src = 'images/tj2.gif']")
    input_answer_loc = ("id", "answer")
    answer_determine_loc = ("css selector", "img[src = 'images/qd.gif']")

    #action
    def forget_name(self, username):
        """Enter username"""
        self.clear_type(self.forget_name_loc, username)
    def forget_submit(self):
        """Click on the submit"""
        self.click(self.forget_submit_loc)
    def input_answer(self,answer):
        """Enter the answer"""
        self.clear_type(self.input_answer_loc, answer)
    def answer_determine(self):
        """Click ok"""
        self.click(self.answer_determine_loc)

    #answer inlet
    def forget_pwd1(self, username=data1[0]['username']):
        """Forget password 1"""
        self.open()
        self.forget_name(username)
        self.forget_submit()
    def forget_pwd2(self, username=data1[0]['username']):
        """Forget password 2"""
        for i in range(3):
            self.forget_name(username)
            self.forget_submit()
    def answer1(self, answer=data1[6]["answer"]):
        """Enter the answer"""
        self.input_answer(answer)
        self.answer_determine()

    #定位器
    username_error_loc = ("id", "usernameId")
    username_succ_loc = ("css selector", "font[class='bold font14']")
    answer_error1_loc = ("id", "answerMsg")
    answer_error2_loc = ("id", "resultMsg")

    #action
    def username_error(self, actual):
        """用户名为空/至少5位数/纯数字/未设置密保/输入错误超过3次"""
        return self.is_text_in_element(self.username_error_loc, actual)
    def username_succ(self, actual):
        """账户正确，进入密保"""
        return self.is_text_in_element(self.username_succ_loc, actual)
    def answer_error1(self, actual):
        """答案为空"""
        return self.is_text_in_element(self.answer_error1_loc, actual)
    def answer_error2(self, actual):
        """超过三次"""
        return self.is_text_in_element(self.answer_error2_loc, actual)


