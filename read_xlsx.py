# -*- coding:utf-8 -*-
import xlrd
import json

ExcelFile = xlrd.open_workbook(r'./贵阳数据离线完成清单.xlsx')
sheet = ExcelFile.sheet_by_index(0)
cols = sheet.col_values(0)
print(len(cols))
dl = []
for j in cols:
    dl.append(j[4:-11])
dicts = []
with open("./task_list.json", "r") as f:
    data = f.read()

li = json.loads(data)
for i in li:
    if i["TRACKPOINTID"] not in dl:
        dicts.append(i)
print(len(dicts))
with open("./task_listss.json", "w") as f:
    f.write(json.dumps(dicts))
