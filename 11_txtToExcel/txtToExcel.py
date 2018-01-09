import pandas as pd

txt_path = r'text.txt'
excel_path = r'excel.xlsx'
xml_path = r'student.xml'

with open(txt_path) as f:
    s = eval(f.read(),{})
    for v in s.values():
        for i in range(len(v)):
            if isinstance(v[i],basestring):
                v[i] = str(v[i]).decode('utf-8')
s = pd.DataFrame(s).T
writer = pd.ExcelWriter(excel_path)
s.to_excel(writer,'student',header = False)
writer.save()

with open("city.txt") as f:
    s = eval(f.read())
s = pd.DataFrame(s,index = [0])
print s
s.T.to_excel("city.xlsx",'city',header=False)

with open("numbers.txt") as f:
    s = eval(f.read())
#pd.DataFrame(s).T.to_excel("nums.xlsx",'num',header = False)

pd.DataFrame(s).T.to_excel(writer,'num',header = False)
writer.save()

import xlrd
import json

data = xlrd.open_workbook(excel_path)
with open(xml_path,'w') as f:
    f.write(r'<?xml version = "1.0" encoding = "UTF-8"?>')
    f.write("\n<root>\n")
    for sheet in data.sheets():
        f.write('<students>\n<!-\n\tstuinfo\n\t"id":[name,math,chn,eng]\n->\n')
        sheet_dict = {}
        for i in range(sheet.nrows):
            sheet_dict[sheet.cell_value(i,0)] = [sheet.cell_value(i,j) for j in range(1,sheet.ncols)]
        s = json.dumps(sheet_dict,ensure_ascii=False,indent=4,sort_keys=True)
        f.write(s.encode('utf-8'))
        f.write("\n</students>\n")
    f.write("<root>")

data = xlrd.open_workbook('city.xlsx')
with open("city.xml",'w') as f:
    f.write(r'<?xml version = "1.0" encoding = "UTF-8"?>')
    f.write("\n<root>\n")
    for sheet in data.sheets():
        f.write('<citys>\n<!-\n\tcityinfo\n->\n')
        sheet_dict = {}
        for i in range(sheet.nrows):
            sheet_dict[sheet.cell_value(i,0)] = sheet.cell_value(i,1)
        s = json.dumps(sheet_dict,ensure_ascii=False,indent=4,sort_keys=True)
        f.write(s.encode('utf-8'))
        f.write("\n</citys>\n")
    f.write("<root>")

data = xlrd.open_workbook('nums.xlsx')
with open("nums.xml",'w') as f:
    f.write(r'<?xml version = "1.0" encoding = "UTF-8"?>')
    f.write("\n<root>\n")
    for sheet in data.sheets():
        f.write('<citys>\n<!-\n\tnuminfo\n->\n')
        sheet_list = []
        for i in range(sheet.nrows):
            sheet_list.append([sheet.cell_value(i,j) for j in range(1,sheet.ncols)])
        s = json.dumps(sheet_list,ensure_ascii=False,indent=4,sort_keys=True)
        f.write(s.encode('utf-8'))
        f.write("\n</citys>\n")
    f.write("<root>")