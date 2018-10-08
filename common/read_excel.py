import os
import xlrd
from xlrd import open_workbook

def readxlrd(sheet,row,col):
    public_dir = os.path.dirname(__file__)
    filename = os.path.join(public_dir,'ceshi.xls')

    data = open_workbook(filename)
    sheet_value = data.sheet_by_index(sheet)
    datarow = sheet_value.row(row)[col].value
    return datarow

#print(readxlrd(0,1,0))