name = '123'


def f1():
    print name


def f2():
    name = '321'
    return f1


li = [lambda :x for x in range(10)]

print li.__len__()
print li[0]()
print li[2]()
# ret = f2()
# ret()
