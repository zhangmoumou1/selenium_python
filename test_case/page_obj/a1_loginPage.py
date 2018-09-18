import sys
sys.path.append('/home/selenium_python')
from data.testdata.data_read import Test1
from public.base import Page
data1 = Test1().a1_data(sheet="a1_sta")

class login(Page):
    """
    User login page
    """
    url = "/u/tologin.do?preUrl=http%3A%2F%2Fwww.cmread.com%2Fu%2Findex"
    #定位器
    login_iframe_loc = ("xpath", "//iframe[contains(@src,'https://wap.cmread.com/sso/auth?e_p=1&response_type=token')]")
    login_username_loc = ("id", "unameInput")
    login_password_loc = ("id", "pwdInput")
    login_button_loc = ("css selector", "input[name = 'login']")
    #Action
    def login_iframe(self):
        self.switch_to_frame(self.login_iframe_loc)
    def login_username(self,username):
        self.clear_type(self.login_username_loc, username)
    def login_password(self,password):
        self.clear_type(self.login_password_loc, password)
    def login_button(self):
        self.click(self.login_button_loc)

    #login inlet
    def user_login(self, username=data1[0]['username'], password=data1[0]['password']):
        """
        User name password login
        """
        self.open()
        self.login_iframe()
        self.login_username(username)
        self.login_password(password)
        self.login_button()

    #定位器
    input_error_loc = ("class name", "wrong")
    user_login_success_loc = ("css selector", "span[title = '好的好的d']")
    #Action
    def user_error_hint(self,actual):
        """用户名输入有误"""
        return self.is_text_in_element(self.input_error_loc, actual)
    def pawd_error_hint(self,actual):
        """密码输入有误"""
        return self.is_text_in_element(self.input_error_loc, actual)
    def user_login_success(self,actual):
        """成功登录获取当前账号"""
        return self.is_text_in_element(self.user_login_success_loc, actual)
