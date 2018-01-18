#coding:utf-8
# tmp = ([1,2],[3,4,5])
# tmp = str(tmp)
# print str(tmp), isinstance(tmp,str),len(tmp)

str1 = "u'\u5317\u4eac\u5317'"
sta = [(u'\u5317\u4eac\u5317', u'VAP'), (u'\u5317\u4eac\u4e1c', u'BOP'), (u'\u5317\u4eac', u'BJP')]
dic_sta = dict(sta)
print dic_sta['北京'.decode('utf-8')]
print dic_sta

print str1