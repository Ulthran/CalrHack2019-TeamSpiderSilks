"""
converter.py

Author: Silas Rhyneer

This program turns a .txt file exported from the carleton calendar into a formatted excel file
"""

import xlwt
import xlrd
import os
directory = 'data'
header = ["name", "date", "link", "startTime", "stopTime", "location", "description", "category"]

try:
    os.remove("yearData.xls")
except:
    pass

"""
Compiles all files onto one .txt file
"""
with open('backSlashFile.txt', 'w') as outfile:
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(directory + "/" + filename) as infile:
                for line in infile:
                    outfile.write(line)
outfile.close()

with open('backSlashFile.txt', 'r') as infile:
    with open('allData.txt', 'w') as outfile:
        for line in infile:
            outfile.write(line.replace("\\", ""))

f = open('allData.txt', 'r')
row_list = []
for row in f:
    # row_list.append(i.replace("#", "").strip("am").strip("pm").strip(" ") for i in row.split(","))
    thisRow = [i for i in row.split(",")]
    #thisRow[4] = function(thisRow[4])
    #thisRow[5] = function(thisRow[5])
    row_list.append(thisRow)
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
    workbook.save('yearData.xls')
    i+=1
