import csv,xlrd
'''
with open('data.xlsx') as f:
    data=csv.excel_tab(f)
    for r in data:
        print(r)
'''
data = xlrd.open_workbook('data.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
title = table.row_values(0)
dataLst = []
for row in range(1,nrows):
    dataDict = {}
    for col in range(ncols):
        value = table.col_values(col)
        dataDict[title[col]] = value[row]
    dataLst.append(dataDict)
        #dataLst.append(dict(zip(title[col],table.col_values(row))))
for i in dataLst:
    print(i['用户名称'])

