#coding:utf-8
# tmp = ([1,2],[3,4,5])
# tmp = str(tmp)
# print str(tmp), isinstance(tmp,str),len(tmp)

# str1 = "u'\u5317\u4eac\u5317'"
# sta = [(u'\u5317\u4eac\u5317', u'VAP'), (u'\u5317\u4eac\u4e1c', u'BOP'), (u'\u5317\u4eac', u'BJP')]
# dic_sta = dict(sta)
# print dic_sta['北京'.decode('utf-8')]
# print dic_sta
#
# print str1

adic = {'1': 50, '4': 20,  '2': 40, '3': 30, '5': 10}
# items = adic.items()
# print(adic)
# print(sorted(adic.keys()))
value_dic = sorted(adic.items(), key=lambda x: x[0])
print(value_dic)