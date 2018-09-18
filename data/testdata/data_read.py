import sys
sys.path.append('/home/selenium_python')
from public.datainfo import ExcelUtil
from config import globalparam

class Test1():
    """Get the excel data"""
    def a1_data(self,sheet):
        """a1_login_sta's values"""
        filepath = globalparam.data_path + "./" + "datas.xlsx"
        sheetName = sheet
        data = ExcelUtil(filepath, sheetName)
        data1 = data.dict_data()
        return data1

# filepath = "F:\git\zhangmoumou1\migu-web-1\data\\testdata\datas.xlsx"
# sheetName = "a1_sta"
# data = ExcelUtil(filepath, sheetName)
# data1 = data.dict_data()
# print(data1[1]['username'])
