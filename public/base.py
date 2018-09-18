import time
import os.path
import sys
sys.path.append('/home/selenium_python')
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from public.log import Log
from config import globalparam

success = "SUCCESS   "
fail = "【FAIL】   "
logger = Log()

class Page():
    """
    页面基础类，用于所有页面的继承

    """
    ai_url = "http://www.cmread.com"
    def __init__(self,selenium_driver,base_url = ai_url,parent = None):
        self.base_url = base_url
        self.driver = selenium_driver
        # self.timeout = 30
        self.parent = parent

    def my_print(self,msg):
        logger.info(msg)

    def fail_img(self):
        file_name = '%s.jpg' % time.strftime("%Y_%m_%d_%H_%M_%S")
        file_path = globalparam.eximg_path + "\\" + file_name
        self.driver.get_screenshot_as_file(file_path)

    def assert_img(self):
        file_name = 'assert(%s).jpg' % time.strftime("%Y_%m_%d_%H_%M_%S")
        file_path = globalparam.eximg_path + "\\" + file_name
        self.driver.get_screenshot_as_file(file_path)

    def select_browser(self,browser='chrome', remoteAddress=None):
        t1 = time.time()
        dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
        dr = None
        if remoteAddress is None:
            if browser == "firefox" or browser == "ff":
                dr = webdriver.Firefox()
            elif browser == "chrome" or browser == "Chrome":
                dr = webdriver.Chrome()
            elif browser == "internet explorer" or browser == "ie":
                dr = webdriver.Ie()
            elif browser == "opera":
                dr = webdriver.Opera()
            elif browser == "phantomjs":
                dr = webdriver.PhantomJS()
            elif browser == "edge":
                dr = webdriver.Edge()
        else:
            if browser == "RChrome":
                dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
                                      desired_capabilities=dc)
            elif browser == "RIE":
                dc['browserName'] = 'internet explorer'
                dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
                                      desired_capabilities=dc)
            elif browser == "RFirefox":
                dc['browserName'] = 'firefox'
                dc['marionette'] = False
                dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
                                      desired_capabilities=dc)
        try:
            self.driver = dr
            self.my_print(
                "{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
        except Exception:
            raise NameError("Not found {0} browser,You can enter 'ie','ff',"
                                "'chrome','RChrome','RIe' or 'RFirefox'.".format(browser))

    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        # assert self.on_page(),"did not land on %s " % url

    def element_wait(self, css, secs=8):
        """
        Waiting for an element to display.

        Usage:
        driver.element_wait("id->kw",10)
        """
        # if "->" not in css:
        #     raise NameError("Positioning syntax errors, lack of '->'.")

        # by = css.split("->")[0].strip()
        # value = css.split("->")[1].strip()
        by = css[0].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)

        if by == "id":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "name":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "class name":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "link text":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "css selector":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        
    def get_element(self, css):
        """
        Judge element positioning way, and returns the element.

        Usage:
        driver.get_element('id->kw')
        """
        # if "->" not in css:
        #     raise NameError("Positioning syntax errors, lack of '->'.")

        # by = css.split("->")[0].strip()
        # value = css.split("->")[1].strip()
        by = css[0].strip()
        value = css[1].strip()
        if by == "id":
            element = self.driver.find_element(by,value)
        elif by == "name":
            element = self.driver.find_element(by,value)
        elif by == "class name":
            element = self.driver.find_element(by,value)
        elif by == "link text":
            element = self.driver.find_element(by,value)
        elif by == "xpath":
            element = self.driver.find_element(by,value)
        elif by == "css selector":
            element = self.driver.find_element(by,value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element
        
    def open(self):
        """
        open url.
        Usage:
        driver.open("http://www.fengsulian.com")
        """
        t1 = time.time()
        nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
        file_name = 'open->%s.jpg' % nowTime
        file_path = globalparam.eximg_path + "\\" + file_name
        try:
            self._open(self.url)
            self.my_print("{0} Navigated to {1}, Spend {2} seconds".format(success,self.base_url+self.url,time.time()-t1))
        except Exception:
            self.my_print("{0} Unable to load {1}, Spend {2} seconds".format(fail,self.base_url+self.url,time.time()- t1))
            self.fail_img()
            raise

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def max_window(self):
        """
        set browser window maximized.
        """
        t1 = time.time()
        self.driver.maximize_window()
        self.my_print("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t1))

    def set_window(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        """
        t1 = time.time()
        self.driver.set_window_size(wide, high)
        self.my_print("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(success,
            wide,high,time.time() - t1))

    def type(self, css, text):
        """
        Operation input box.

        Usage:
        driver.type("id->kw","selenium")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        base_dir = print(os.path.dirname(os.path.abspath(__file__)))
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.send_keys(text)
            self.my_print("{0} Typed element: <{1}> content: {2}, Spend {3} seconds -- from{4}".format(success,
                css1,text,time.time() - t1,base_dir))
        except Exception:
            self.my_print("{0} Unable to type element: <{1}> content: {2}, Spend {3} seconds-- from{4}".format(fail,
                css1, text, time.time() - t1,base_dir))
            self.fail_img()
            raise
        
    def clear_type(self, css, text):
        """
        Clear and input element.

        Usage:
        driver.clear_type("id->kw","selenium")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.clear()
            el.send_keys(text)
            self.my_print("{0} Clear and type element: <{1}> content: {2}, Spend {3} seconds".format(success,
                css1, text,time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to clear and type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                css1, text,time.time() - t1))
            self.fail_img()
            raise
        
    def click(self, css):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]


        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.click()
            self.my_print("{0} Clicked element: <{1}>, Spend {2} seconds".format(success,css1,time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, css1, time.time() - t1))
            self.fail_img()
            raise
        
    def right_click(self, css):
        """
        Right click element.

        Usage:
        driver.right_click("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).context_click(el).perform()
            self.my_print("{0} Right click element: <{1}>, Spend {2} seconds".format(success, css1, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, css1, time.time() - t1))
            self.fail_img()
            raise
    
    def move_to_element(self, css):
        """
        Mouse over the element.

        Usage:
        driver.move_to_element("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).move_to_element(el).perform()
            self.my_print("{0} Move to element: <{1}>, Spend {2} seconds".format(success, css1, time.time() - t1))
        except Exception:
            self.my_print("{0} unable move to element: <{1}>, Spend {2} seconds".format(fail, css1, time.time() - t1))
            self.fail_img()
            raise
        
    def double_click(self, css):
        """
        Double click element.

        Usage:
        driver.double_click("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).double_click(el).perform()
            self.my_print("{0} Double click element: <{1}>, Spend {2} seconds".format(success, css1, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, css1, time.time() - t1))
            self.fail_img()
            raise

    def drag_and_drop(self, el_css, ta_css):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("id->kw","id->su")
        """
        t1 = time.time()
        try:
            self.element_wait(el_css)
            element = self.get_element(el_css)
            self.element_wait(ta_css)
            target = self.get_element(ta_css)
            ActionChains(self.driver).drag_and_drop(element, target).perform()
            self.my_print("{0} Drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(success,
                el_css,ta_css, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(fail,
                el_css, ta_css, time.time() - t1))
            self.fail_img()
            raise
        
    def click_text(self, text):
        """
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        """
        t1 = time.time()
        try:
            self.driver.find_element_by_partial_link_text(text).click()
            self.my_print("{0} Click by text content: {1}, Spend {2} seconds".format(success, text,time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to Click by text content: {1}, Spend {2} seconds".format(fail, text, time.time() - t1))
            self.fail_img()
            raise
        
    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        """
        t1 = time.time()
        self.driver.close()
        self.my_print("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        t1 = time.time()
        self.driver.quit()
        self.my_print("{0} Closed all window and quit the driver, Spend {1} seconds".format(success, time.time() - t1))

    def submit(self, css):
        """
        Submit the specified form.

        Usage:
        driver.submit("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.submit()
            self.my_print("{0} Submit form args element: <{1}>, Spend {2} seconds".format(success,css1, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to submit form args element: <{1}>, Spend {2} seconds".format(fail, css1, time.time() - t1))
            self.fail_img()
            raise

    def F5(self):
        """
        Refresh the current page.

        Usage:
        driver.F5()
        """
        t1 = time
        self.driver.refresh()
        self.my_print("{0} Refresh the current page, Spend {1} seconds".format(success, time.time() - t1))

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            self.my_print("{0} Execute javascript scripts: {1}, Spend {2} seconds".format(success,script, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail,
                script, time.time() - t1))
            self.fail_img()
            raise

    def get_attribute(self, css, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("id->su","href")
        """
        t1 = time.time()
        try:
            el = self.get_element(css)
            attr = el.get_attribute(attribute)
            self.my_print("{0} Get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(success,
                css,attribute,time.time()-t1))
            return attr
        except Exception:
            self.my_print("{0} Unable to get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(fail,
                css, attribute,time.time() - t1))
            self.fail_img()
            raise

    def get_text(self, css):
        """
        Get element text information.

        Usage:
        driver.get_text("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            text = self.get_element(css).text
            self.my_print("{0} Get element text element: <{1}>, Spend {2} seconds".format(success,css1,time.time()-t1))
            return text
        except Exception:
            self.my_print("{0} Unable to get element text element: <{1}>, Spend {2} seconds".format(fail, css1, time.time() - t1))
            self.fail_img()
            raise

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """

        t1 = time.time()
        title = self.driver.title
        self.my_print("{0} Get current window title, Spend {1} seconds".format(success, time.time() - t1))
        return title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        t1 = time.time()
        url = self.driver.current_url
        self.my_print("{0} Get current window url, Spend {1} seconds".format(success, time.time() - t1))
        return url

    def wait(self, secs):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        t1 = time.time()
        self.driver.implicitly_wait(secs)
        self.my_print("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success,
            secs,time.time() - t1))

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        driver.accept_alert()
        """
        t1 = time.time()
        self.driver.switch_to.alert.accept()
        self.my_print("{0} Accept warning box, Spend {1} seconds".format(success, time.time() - t1))

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        """
        t1 = time.time()
        self.driver.switch_to.alert.dismiss()
        self.my_print("{0} Dismisses the alert available, Spend {1} seconds".format(success, time.time() - t1))

    def switch_to_frame(self, css):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            iframe_el = self.get_element(css)
            self.driver.switch_to.frame(iframe_el)
            self.my_print("{0} Switch to frame element: <{1}>, Spend {2} seconds".format(success,css1, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable switch to frame element: <{1}>, Spend {2} seconds".format(fail, css1, time.time() - t1))
            self.fail_img()
            raise

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        t1 = time.time()
        self.driver.switch_to.default_content()
        self.my_print("{0} Switch to frame out, Spend {1} seconds".format(success, time.time() - t1))

    def open_new_window(self, css):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            original_windows = self.driver.current_window_handle
            el = self.get_element(css)
            el.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            self.my_print("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(success,
                css1,time.time() - t1))
        except Exception:
            self.my_print("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(fail,
                css1,time.time() - t1))
            self.fail_img()
            raise

    def element_exist(self, css):
        """
        judge element is exist,The return result is true or false.

        Usage:
        driver.element_exist("id->kw")
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            self.my_print("{0} Element: <{1}> is exist, Spend {2} seconds".format(success,css1, time.time() - t1))
            return True
        except TimeoutException:
            self.my_print("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, css1, time.time() - t1))
            self.fail_img()
            return False

    def take_screenshot(self, file_path):
        """
        Get the current window screenshot.

        Usage:
        driver.take_screenshot('c:/test.png')
        """
        t1 = time.time()
        try:
            self.driver.get_screenshot_as_file(file_path)
            self.my_print("{0} Get the current window screenshot,path: {1}, Spend {2} seconds".format(success,
                file_path, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to get the current window screenshot,path: {1}, Spend {2} seconds".format(fail,
                file_path,time.time() - t1))
            self.fail_img()
            raise

    def into_new_window(self):
        """
        Into the new window.

        Usage:
        dirver.into_new_window()
        """
        t1 = time.time()
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                time.sleep(1)
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handle[-1])
            self.my_print("{0} Switch to the new window,new window's url: {1}, Spend {2} seconds".format(success,
                self.driver.current_url,time.time() - t1))
        except Exception:
            self.my_print("{0} Unable switch to the new window, Spend {1} seconds".format(fail, time.time() - t1))
            self.fail_img()
            raise

    def type_and_enter(self, css, text, secs=0.5):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.

        Usage:
        driver.type_css_keys('id->kw','beck')
        """
        t1 = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait(css)
            ele = self.get_element(css)
            ele.send_keys(text)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
            self.my_print("{0} Element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".format(
                success,css1,text,secs,time.time() - t1))
        except Exception:
            self.my_print("{0} Unable element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".
                format(fail, css1, text, secs, time.time() - t1))
            self.fail_img()
            raise

    def js_click(self, css):
        """
        Input a css selecter,use javascript click element.

        Usage:
        driver.js_click('#buttonid')
        """
        t1 = time.time()
        js_str = "$('{0}').click()".format(css)
        try:
            self.driver.execute_script(js_str)
            self.my_print("{0} Use javascript click element: {1}, Spend {2} seconds".format(success,js_str,time.time()-t1))
        except Exception:
            self.my_print("{0} Unable to use javascript click element: {1}, Spend {2} seconds".format(fail,
                js_str, time.time() - t1))
            self.fail_img()
            raise

    def scroll_bar(self,horizontal,vertical):
        """
        Control scrollbar
        """
        return self.driver.execute_script(self.window.scrollTo(horizontal,vertical))


    def find_elements(self,*loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            print("%s cannot find elements %s in page." % (self,loc))

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
        Usage:
        result = driver.text_in_element(locator, text)
        """
        t1 = time.time()
        locator1 = locator[0] + "->" + locator[1]
        try:
            result = WebDriverWait(self.driver, timeout, 0.5).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self.my_print("{0} element not positioned: <{1}> , Spend {2} seconds".format(fail,
                                                                                         locator1, time.time() - t1))
            self.fail_img()
            return False
        else:
            self.my_print("{0} positioned to element: <{1}> , Spend {2} seconds".format(success,
                                                                                       locator1, time.time() - t1))
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        Usage:
        result = driver.text_in_element(locator, text)
        """
        t1 = time.time()
        locator1 = locator[0] + "->" + locator[1]
        try:
            result = WebDriverWait(self.driver, timeout, 0.5).until(EC.text_to_be_present_in_element_value(locator,
                                                                                                         value))
        except TimeoutException:
            self.my_print("{0} element not positioned: <{1}> , Spend {2} seconds".format(fail,
                                                                                         locator1, time.time() - t1))
            self.fail_img()
            return False
        else:
            self.my_print("{0} positioned to element: <{1}> , Spend {2} seconds".format(success,
                                                                                       locator1, time.time() - t1))
            return result

    def assert_equal(self,loc,text):
        """
        say with certainty

        Usage:
        assertNotEqual(loc,text)
        """
        t1 = time.time()
        try:
            self.assertEqual(loc,text)
            self.my_print("{0} say with certainty: {1} == {2}, Spend {3} seconds".format(success,loc,
                                                                                         text,time.time()-t1))
        except Exception:
            self.my_print("{0} say with certainty: {1} != {2}, Spend {3} seconds".format(fail, loc,
                                                                                         text, time.time() - t1))
            self.assert_img()
            raise

    def assert_notequal(self, loc, text):
        """
        say with certainty

        Usage:
        assertEqual(loc,text)
        """
        t1 = time.time()
        try:
            self.assertNotEqual(loc, text)
            self.my_print("{0} say with certainty: {1} != {2}, Spend {3} seconds".format(success, loc,
                                                                                         text, time.time() - t1))
        except:
            self.my_print("{0} say with certainty: {1} == {2}, Spend {3} seconds".format(fail, loc,
                                                                                         text, time.time() - t1))
            self.assert_img()
            raise

    def js1(self,css):
        """
        Handle the target property as empty

        """
        css1 = css[0].capitalize()
        css2 = css[1]
        css3 = css[0] + "->" + css[1]
        t1 = time.time()
        try:
            ele = "document.getElementBy{0}({1}).target=' ';" .format(css1, css2)
            self.driver.execute_script(ele)
        except:
            self.my_print("{0} positioned to element: <{1}> , Spend {2} seconds".format(success,
                                                                                        css3, time.time() - t1))