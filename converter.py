"""
converter.py

Author: Silas Rhyneer

This program turns a .txt file exported from the carleton calendar into a formatted excel file
"""

import xlwt
import xlrd
f = open('text.txt', 'r')

header = ["name", "date", "link", "startTime", "stopTime", "location", "description"]

row_list = []
for row in f:
    row_list.append(i.replace("#", "").strip(" am").strip(" pm") for i in row.split(","))
column_list = zip(*row_list)
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet1')
i = 1
j = 0

for title in header:
    j+=1
    worksheet.write(0, j, title)

for column in column_list:
    for item in range(len(column)):
        print(column[item])
        worksheet.write(item+1, i, column[item])
    workbook.save('Excel.xls')
    i+=1
