# coding:utf-8
import xlrd
class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # Get the first row as the key value
        self.keys = self.table.row_values(0)
        # Get the total number of rows
        self.rowNum = self.table.nrows
        # Get the total number of columns
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

# if __name__ == "__main__":
#     filepath = "F:\\Git\\migu-web\\data\\testdata\datas.xlsx"
#     sheetName = "a1_sta"
#     data = ExcelUtil(filepath, sheetName)
# print(data.dict_data())

