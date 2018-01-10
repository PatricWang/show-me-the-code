[python Offical Doc](https://docs.python.org/2/contents.html)

1.将图片右上角加上红色的数字，类似于微信未读信息数量那种提示效果
--

[python中import自己写的.py](http://blog.csdn.net/AlanConstantineLau/article/details/68952256)

[pillow reference](http://pillow.readthedocs.io/en/5.0.0/)

2.生成激活码(随机字母序列，cdkey）并存入数据库(mysql,redis)
--

[numpy reference](https://docs.scipy.org/doc/numpy/reference/)

string

![](https://github.com/PatricWang/show-me-the-code/blob/master/2_gen_ticket/string.JPG)


[range用法](https://www.cnblogs.com/buro79xxd/archive/2011/05/23/2054493.html)

[yeild怎么用](https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)

[windows下安装redis](https://www.cnblogs.com/M-LittleBird/p/5902850.html)

windows下安装MySql从官网直接下

3.任一个英文的纯文本文件，统计其中的单词出现的个数
--

### import:<br>

sklearn
[sklearn reference](http://scikit-learn.org/stable/index.html)  [中文](http://sklearn.apachecn.org/cn/stable/index.html)

### keyword & fct:<br>
`open`:打开文件<br>
常用模式：<br>
r：从开头只读<br>
r+：从开头读写<br>
w：只写，如果文件存在则将其覆盖，如果不存在则创建新文件<br>
w+：读写，如果文件存在则将其覆盖，如果不存在则创建新文件<br>
a：从文件结尾处开始写，如果不存在则创建新文件<br>
a+：从文件结尾处读写，如果不存在则创建新文件<br>

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

* #### **[code explanation](https://app.yinxiang.com/shard/s72/nl/17217582/1b467e80-0ed2-445c-af4f-038f671c2d6c)**


4.你有一个目录，装了很多照片，把它们的尺寸变成指定大小。
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

5.从一个网站上爬取所有文章然后统计出每篇文章最重要的词。
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


* #### **[code explanation](https://app.yinxiang.com/shard/s72/nl/17217582/9314eb53-b6c9-4f77-8b51-c9dd7056ed5a)**


6.统计一个目录下有多少cpp文件，多少行代码，空行和注释
--

### keyword & fct:<br>
`str.strip()`:<br>用于移除字符串头尾指定的字符（默认为空格）<br>

7.一个HTML文件，找出里面的正文和链接
--

### others:<br>

**python write 和 writelines的区别**：<br>

file.write(str)的参数是一个字符串，就是你要写入文件的内容.<br>
file.writelines(sequence)的参数是序列，比如列表，它会迭代帮你写入文件。<br>

8.生成随机验证码
--

### keyword & fct:<br>
`random.choice()`:<br>返回一个列表，元组或字符串的随机项<br>
`ImageFont.truetype(font=None, size=10, index=0, encoding='', layout_engine=None):`<br>
加载一个TrueType或者OpenType字体文件，并且创建一个字体对象。这个函数从指定的文件加载了一个字体对象，并且为指定大小的字体创建了字体对象<br>
`Image.new(mode, size, color=0)`:<br>新建一个Image
`ImageDraw.Draw(im, mode=None)`:<br>Creates an object that can be used to draw in the given image.<br>
`enumerate(sequence, [start=0])`:<br>函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中<br>
```python
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 小标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```
`randrange([start,] stop [,step])`:<br>:返回指定递增基数集合中的一个随机数，基数缺省值为1<br>


9.敏感词文本文件 filtered_words.txt，里面的内容固定，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
--

### new import:<br>
`sys`:<br>This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.<br>这个模块可供访问由解释器使用或维护的变量和与解释器进行交互的函数。<br>
`local`:<br>opens access to the POSIX locale database and functionality. The POSIX locale mechanism allows programmers to deal with certain cultural issues in an application, without requiring the programmer to know all the specifics of each country where the software is executed.<br>


10.保存链接中的图片
--

### new import:<br>
`requests`:<br>http库
`lxml.html`:<br>解析html,[lxml.html](http://lxml.de/lxmlhtml.html)<br>


### keyword & fct:<br>
`requests.get(url)`:<br>发送http请求，返回response对象<br>
`lxml.html.document_fromstring(str)`:<br>由给定的参数生成一个HtmlElement对象<br>
`cssselect(str)`:<br>通过ccs选择器定位<br>

* #### **[code explanation](https://app.yinxiang.com/shard/s72/nl/17217582/d554182e-3419-42a4-9edb-74f06039c858)**


11.txt转为excel,excel转为xml
--

### new import:<br>
`pandas`:<br>
Python Data Analysis Library<br>
[10 Minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)<br>
[cookbook](http://pandas.pydata.org/pandas-docs/stable/cookbook.html#cookbook)<br>
`xlrd`:<br>Library for developers to extract data from Microsoft Excel (tm) spreadsheet files<br>
[doc](http://xlrd.readthedocs.io/en/latest/)
`json`:<br>编码和解码json对象, JavaScript Object Notation, 是一种轻量级的数据交换格式，易于人阅读和编写。<br>


### keyword & fct:<br>
`eval（expression，globals=None, locals=None）`:<br>
将字符串str当成有效的表达式来求值并返回计算结果，可以将字符串转成list,tuple,dict<br>
`dict.values()`:<br>
返回字典中的所有值<br>
`numpy.random.rand(d0,d1...dn)`:<br>
Create an array of the given shape and propagate it with random samples from a uniform distribution over \[0, 1).<br>
`pandas.DataFrame.to_excel`:<br>
DataFrame转为excel
`xlrd.open_workbook(excel_path)`:<br>Open a spreadsheet file for data extraction<br>
Returns:	An instance of the Book class.<br>
`book.sheets()`:<br>Returns:	A list of all sheets in the book<br>
`sheet.cell_value(i,j)`:<br>Value of the cell in the given row and column.<br>
`sheet.nrows`:number of rows<br>
`sheet.ncols`:number of cols<br>
`json.dumps(obj)`:将 Python 对象编码成 JSON 字符串<br>
`json.loads()`:将已编码的 JSON 字符串解码为 Python 对象<br>

12.使用 Python 对密码加密
--

### new import:<br>
`hashlib`:<br>提供了常见的摘要算法，如MD5，SHA1等等。<br>
什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。<br>
摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。<br>
摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。<br>
`hmac`:<br>实现了hmac算法，需要一个key来进行加密, Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。<br>


### keyword & fct:<br>
`os.urandom(n)`:<br>随即产生n个字节的字符串，可以作为随机加密key使用
`hmac.digest()`:<br>
Return the hash value of this hashing object.<br>
This returns a string containing 8-bit data. The object is not altered in any way by this function; you can continue updating the object after calling this function<br>

13.A Simple Web Server
--

一般我们的web程序都运行在 TCP/IP 协议上，程序之间使用 socket(套接字) 进行通信，它能够让计算机之间的通信就像写文件和读文件一样简单。<br>
一个 tcp socket 由一个IP地址和端口号组成。<br>
IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”,写成10进制的形式就是我们常见的 174.136.14.108。我们通过IP地址来标识所连接的主机。<br>
端口号是一个范围在0-65535之间的数字，一台主机上可能同时有多个sockets，因此需要端口号进行标识。端口号0-1023 是保留给操作系统使用的，我们可以使用剩下的端口号。<br>
超文本传输协议（HTTP）描述了一种程序之间交换数据的方法，它非常简单易用，在一个socket连接上，客户端首先发送请求说明它需要什么，然后服务器发送响应，并在响应中包含客户端的数据。响应数据也许是从本地磁盘上复制来的，也许是程序动态生成的。<br>


[原文link](http://www.aosabook.org/en/500L/a-simple-web-server.html)

### new import:<br>
`BaseHTTPServer`:<br>基本的 HTTP 服务器, 这个模块定义了两个实现 HTTP 服务器 (Web 服务器)的类。 通常地， 这个模块不被直接使用，但被用来作为构建功能性 Web 服务器的一个基类<br>
第一个类， HTTPServer， 是 SocketServer.TCPServer 的一个子类。它创建并监听HTTP socket， 发送请求到一个处理程序。<br>
第二个类， BaseHTTPRequestHandler(request, client_address, server)<br>
这个类被用来处理到达服务器的 HTTP 请求。单独地，它不能响应任意实际的 HTTP 请求，必须是子类来处理每个请求方法 (例如， GET 或 POST)。BaseHTTPRequestHandler provides a number of class and instance variables, and methods for use by subclasses.<br>

### keyword & fct:<br>
`send_response(code)`<br>
`send_header(keyword, value)`<br>
`end_headers()`<br>































