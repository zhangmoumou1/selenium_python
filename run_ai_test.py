# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from config import globalparam
import unittest
import time

test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="*sta.py")

if __name__ == "__main__":
    # Get the current time in a certain format
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # Define the report storage path
    filename = globalparam.report_path + "\\" + now + "result.html"
    fp = open(filename, "wb")
    # Define test report
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况:")
    runner.run(discover)
    fp.close()

