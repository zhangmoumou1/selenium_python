from config import globalparam
from public.base import Page

def insert_img(driver,file_name):
    """Screenshot function"""
    file_path = globalparam.img_path + "\\" + file_name
    Page(driver).take_screenshot(file_path)

