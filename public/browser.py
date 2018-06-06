from selenium import webdriver

def select_browser(browser='chrome', remoteAddress=None):
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
    return dr
