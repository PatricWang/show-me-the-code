[python Offical Doc](https://docs.python.org/2/contents.html)

将图片右上角加上红色的数字，类似于微信未读信息数量那种提示效果
--

[python中import自己写的.py](http://blog.csdn.net/AlanConstantineLau/article/details/68952256)

[pillow reference](https://pillow.readthedocs.io/en/4.3.x/)

生成激活码(随机字母序列，cdkey）并存入数据库(mysql,redis)
--

[numpy reference](https://docs.scipy.org/doc/numpy/reference/)

string

![](https://github.com/PatricWang/show-me-the-code/blob/master/2_gen_ticket/string.JPG)


[range用法](https://www.cnblogs.com/buro79xxd/archive/2011/05/23/2054493.html)

[yeild怎么用](https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)

[windows下安装redis](https://www.cnblogs.com/M-LittleBird/p/5902850.html)

windows下安装MySql从官网直接下

任一个英文的纯文本文件，统计其中的单词出现的个数
--

### import:<br>

sklearn
[sklearn reference](http://scikit-learn.org/stable/index.html)  [中文](http://sklearn.apachecn.org/cn/stable/index.html)

### keyword & fct:<br>
`open`:打开文件<br>
`with-as`:适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等<br>
`read()`:读所有内容，放到字符串中<br>
`readline()`:读一行,<br>
`readlines()`:读所有内容，生成一个行的列表(list)，可以用for...in处理<br>
`numpy.sum()`:返回类型为`numpy.ndarray`<br>
`sorted()`:<br>
**sort 与 sorted 区别:<br>**
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。<br>
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。<br>
sorted(iterable, cmp=None, key=None, reverse=False)<br>
1.cmp，比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0<br>
2.key，主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序<br>
3.reverse，是否反转，默认情况下不反转(从小到大排列)<br>
`zip()`:<br>
This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The returned list is truncated in length to the length of the shortest argument sequence. When there are multiple arguments which are all of the same length, zip() is similar to map() with an initial argument of None. With a single sequence argument, it returns a list of 1-tuples. With no arguments, it returns an empty list.<br>
`lambda表达式`:labmda x : f(x)，举例：<br>
```python
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)
```
[18, 9, 24, 12, 27]<br>
```python
print map(lambda x: x * 2 + 10, foo)
```
[14, 46, 28, 54, 44, 58, 26, 34, 64]<br>
```python
print reduce(lambda x, y: x + y, foo)
```
139<br>

### other:<br>
字符串前加r，防止字符转义
字符串前加u，unicode字符串

[稀疏矩阵csr_matrix](https://app.yinxiang.com/shard/s72/nl/17217582/4de137bc-df5d-45ce-a735-0c53b89aec0a)


[numpy.sum(axis=0)解释](https://segmentfault.com/q/1010000010111006/a-1020000010131823):<br>
简单说对于二维数组，axis=0 按列相加，axis=1 按行相加，详细解释看上面链接

[code explanation](https://app.yinxiang.com/shard/s72/nl/17217582/1b467e80-0ed2-445c-af4f-038f671c2d6c)


你有一个目录，装了很多照片，把它们的尺寸变成指定大小。
--

### new import:<br>
`os`:os 模块提供了一个统一的操作系统接口函数, 这些接口函数通常是平台指定的,os 模块能在不同操作系统平台如 nt 或 posix中的特定函数间自动切换,从而能实现跨平台操作, `os.name`字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。<br>

### keyword & fct:<br>
`os.walk()`:生成一个目录树下的所有文件名<br>
函数原型：<br>
os.walk(top [, topdown = True [, onerror = None [, followlinks = False]]])<br>
参数说明：<br> 
top表示需要遍历的目录树的路径。 <br>
topdown的默认值是“True”，表示首先返回目录树下的文件，然后遍历目录树下的子目录。值设为False时，则表示先遍历目录树下的子目录，返回子目录下的文件，最后返回根目录下的文件。 <br>
onerror的默认值是“None”，表示忽略文件遍历时产生的错误。如果不为空，则提供一个自定义函数提示错误信息后继续遍历或抛出异常中止遍历。 <br>
该函数返回一个列表，列表中的每一个元素都是一个元组，该元组有3个元素，分别表示每次遍历的路径名，目录列表和文件列表。<br>

`os.path.join(path,name)`:连接目录与文件名或目录<br>
```python
>>> os.path.join('c:\\Python','a.txt')
'c:\\Python\\a.txt'
>>> os.path.join('c:\\Python','f1')
'c:\\Python\\f1'
```

从一个网站上爬取所有文章然后统计出每篇文章最重要的词。
--

### new import:<br>
`beautiful soap`:解析HTML和XML<br>
[documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
HTML文件其实就是由一组尖括号构成的标签组织起来的，每一对尖括号形式一个标签，标签之间存在上下关系，形成标签树；因此可以说Beautiful Soup库是解析、遍历、维护“标签树”的功能库。

`urllib2`<br>
`goose`<br>
Python-goose项目是用Python重写的Goose，Goose原来是用Java写的文章提取工具。Python-goose的目标是给定任意资讯文章或者任意文章类的网页，不仅提取出文章的主体，同时提取出所有元信息以及图片等信息，支持中文网页。<br>
[goose on github](https://github.com/grangier/python-goose)<br>

`jieba`:<br>
中文分词组件，[github adr](https://github.com/fxsjy/jieba)<br>
`TfidfTransformer`:统计词语的tfidf权重，[TFIDF介绍](http://blog.csdn.net/eastmount/article/details/50323063)

### keyword & fct:<br>
`urlopen(url)`:Open the URL url, which can be either a string or a Request object,This function returns a file-like object<br>
`urllib2.splittype(url)`<br>
`urllib2.splithost(rest)`<br>
`list.extend(seq)`:<br>
用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）<br>
`decode`:<br>
python使用unicode作为基础编码类型，字符串常用编码utf8,gbk等，编码解码都要通过unicode类型，pyton3中str替代了unicode<br>
[说明](http://blog.csdn.net/moodytong/article/details/8136258)<br>

























