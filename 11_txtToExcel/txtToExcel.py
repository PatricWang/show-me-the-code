import pandas as pd

txt_path = r'text.txt'
excel_path = r'excel.xlsx'

with open(txt_path) as f:
    s = eval(f.read(),{})
    for v in s.values():
        for i in range(len(v)):
            if isinstance(v[i],basestring):
                v[i] = str(v[i]).decode('utf-8')
s = pd.DataFrame(s).T
s.to_excel(excel_path,'student',header = False)
