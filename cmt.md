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
<span id = "jump"></span>
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

#### 用socket写client&server

* **server:**<br>
1.建立一个基于tcp协议的socket对象<br>
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
AF_INET指定ipv4协议，SOCK_STREAM指面向流的tcp协议<br>

2.绑定地址和端口<br>
```python
s.bind(‘’, 8089))
```
引号为空指绑定任意ip，即可接收任意ip的请求，端口号<65535,小于1024时需要管理员权限<br>

3.监听连接请求<br>
```python
s.listen(5)
```
指定最大连接数为5<br>

4.阻塞线程，直到获得客户端连接<br>
```python
sock, addr = s.accept()
```
返回客户端的socket对象和客户端ip&端口，该方法会**阻塞线程**<br>

* **client:**<br>
1.建立socket对象，同server<br>

2.连接到服务器<br>
```python
s.connect(('127.0.0.1', 80))
```

3.发送数据<br>
```python
s.send('hello')
```
tcp连接是双向的，双方都可以给对方发数据<br>

4.接受数据<br>
```python
s.recv(1024)
```
接受对方发来的数据，该方法会**阻塞线程**，所以需要一个专门的线程来接受数据<br>

14.使用socket编写聊天工具
--

实现客户端-服务器-客户端的通信过程，即有两个客户端，这两个客户端可以通过连接服务器进行交互

### keyword & fct:<br>
`setDaemon(bool)`:<br>
将线程声明为守护线程，必须在start()方法调用之前设置，如果不设置为守护线程程序会被无限挂起。这个方法基本和join是相反的。当我们在程序运行中，执行一个主线程，如果方线程又创建一个子线程，主线程和子线程就会分兵两路，分别运行，那么当主线程完成想退出时，会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以用setDaemon方法了<br>
`finally`:<br>
不管异常发生与否，finally下的语句都会执行


### others:<br>
创建一个类：<br>
```python
classs ClassName(BaseClass):
   def __init__(self):
   ...
```
* BaseClass是需要继承的基类，如果不需要继承则不用写括号<br>
* __init__()是构造函数，创建类的实例时会调用<br>
* 类的方法的第一个参数一定是self，代表类的实例，**self不是python的关键字**<br>
* 基类的构造函数不会在派生类中自动调用<br>

15.2048
--


### new import:<br>


`curses`:<br>Terminal handling for character-cell displays<br>
可以用来设置光标的位置和终端屏幕上显示的字符样式。<br>
curses是linux库，官方的是不支持windows的，python会自带curses但是不能直接用，需要搞一个[unoffical](https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses)的库，在里面找到和自己python对应版本的库下下来用pip安装后才可以用,文件名里面的cp27对应python2.7，cp36对应python3.6<br>


python curses库的[manual](https://docs.python.org/2.7/library/curses.html)<br>


`copy`:<br>
[copy和deepcopy的区别](http://blog.csdn.net/qq_32907349/article/details/52190796)

### keyword & fct:<br>

`curses.initscr()`:<br>
Initialize the library. Return a WindowObject which represents the whole screen.<br>
`window.addstr(str)`:<br>
Paint the string str at (y, x) with attributes attr, overwriting anything previously on the display.<br>
`window.refresh()`:<br>
Update the display immediately (sync actual screen with previous drawing/deleting methods).<br>
`window.nodelay(yes)`:<br>
If yes is 1, getch() will be non-blocking.<br>
`window.noecho()`:<br>关闭回显
`curses.cbreak()`:<br>应用程序一般是立即响应的，即不需要按回车就立即回应的，这种模式叫cbreak模式，相反的常用的模式是缓冲输入模式<br>
`curses.wrapper(fun)`:<br>
Initialize curses and call another callable object, func, which should be the rest of your curses-using application. If the application raises an exception, this function will restore the terminal to a sane state before re-raising the exception and generating a traceback. The callable object func is then passed the main window ‘stdscr’ as its first argument, followed by any other arguments passed to wrapper(). Before calling func, wrapper() turns on cbreak mode, turns off echo, enables the terminal keypad, and initializes colors if the terminal has color support. On exit (whether normally or by exception) it restores cooked mode, turns on echo, and disables the terminal keypad.


multithreading & multiprocessing
--

#### 使用多线程的两种方法
1. 直接用threading.Thread创建线程，target指向要执行的函数，args指向函数的参数列表
```python
t1 = threading.Thread(target=run,args=(1,))
t1.start()
```

2. 继承threading.Thread类，重写run方法
```python
class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print 'number:%s' % self.num
        time.sleep(2)
```

### new import:<br>
`threading`:<br>使用threading.Thread来创建线程
`Queue`:<br>队列
`threadpool`:<br>
我们知道系统处理任务时，需要为每个请求创建和销毁对象。当有大量并发任务需要处理时，再使用传统的多线程就会造成大量的资源创建销毁导致服务器效率的下降。这时候，线程池就派上用场了。线程池技术为线程创建、销毁的开销问题和系统资源不足问题提供了很好的解决方案。<br>
1. 可以控制产生线程的数量。通过预先创建一定数量的工作线程并限制其数量，控制线程对象的内存消耗。<br>
2. 降低系统开销和资源消耗。通过对多个请求重用线程，线程创建、销毁的开销被分摊到了多个请求上。另外通过限制线程数量，降低虚拟机在垃圾回收方面的开销。<br>
3. 提高系统响应速度。线程事先已被创建，请求到达时可直接进行处理，消除了因线程创建所带来的延迟，另外多个线程可并发处理。<br>


### keyword & fct:<br>
`join()`:<br>阻塞主线程直到子线程执行结束
`setDaemon(True)`:<br>设置为守护线程，在主线程结束时守护进程也会一同结束，不论有没有执行完<br>
`threading.Lock()`:<br>互斥锁，防止多个线程同时访问同一个变量，非递归，同一个线程中只能acquire一次，acquire多次会死锁<br>
`threading.RLock()`:<br>可递归，同一个线程中可多次acquire<br>
`threading.Semaphore()`:<br>是一个变量，控制着对公共资源或者临界区的访问。信号量维护着一个计数器，指定可同时访问资源或者进入临界区的线程数。 
每次有一个线程获得信号量时，计数器-1。若计数器为0，其他线程就停止访问信号量，直到另一个线程释放信号量。 <br>
`threading.BoundedSemaphore()`:<br> 会检查内部计数器的值，并保证它不会大于初始值，如果超了，就引发一个 ValueError<br>
```python
def foo():
    time.sleep(2)   #程序休息2秒
    print("ok",time.ctime())

for i in range(20):
    t1=threading.Thread(target=foo,args=()) #实例化一个线程
    t1.start()  #启动线程
```
程序会在很短的时间内生成20个线程来打印一句话。<br>
如果在主机执行IO密集型任务的时候再执行这种类型的程序时，计算机就有很大可能会宕机。<br>
**[计算密集型&IO密集型](http://blog.csdn.net/zyy1178625607/article/details/61200263)**
`threading.Event()`:<br>用于主线程控制其他线程的执行，事件处理的机制：全局定义了一个"Flag"，如果"Flag"值为False，那么当程序执行event.wait方法时就会阻塞，如果"Flag"值为True，那么event.wait方法时便不再阻塞。<br>
事件主要提供了三个方法 set、wait、clear:<br>
`clear()`:将"Flag"设置为False<br>
`set()`:将"Flag"设置为True<br>
`wait()`:用在子线程中，调用时根据Flag的值来决定是否阻塞线程
```python
def do(event):
    print 'start'
    event.wait()
    print 'execute'

event_obj = threading.Event()

def test_event():
    for i in range(5):
        t = threading.Thread(target=do, args=(event_obj,))
        t.start()
    event_obj.clear()
    inpt = raw_input('input:')
    if inpt == '1':
        event_obj.set()
```

####生产者消费者模型<br>
生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。<br>

```python
q = Queue.Queue(maxsize=10)
def producer():
    count = 1
    while True:
        q.put('product %s' % count)
        print 'has product', count
        count += 1
        time.sleep(0.1)

def consumer(n):
    while True:
        print '%s consume %s' % (n,q.get())
        time.sleep(0.5)

def test_product_consumer():
    p = threading.Thread(target=producer,)
    c1 = threading.Thread(target=consumer,args=('tom',))
    c2 = threading.Thread(target=consumer,args=('jack',))
    p.start()
    c1.start()
    c2.start()
```

`threadpool.ThreadPool(10)`:<br>建立线程池，控制线程数量为10<br>
`threadpool.makeRequests(callable, args_list, callback)`:<br>
构建请求，callable为要运行的函数，args_list为要多线程执行函数的参数, 最后这个callback是可选的，是对前两个函数运行结果的操作 <br>
**[对args_list的解释](http://bbs.csdn.net/topics/391886273)**:<br>
``args_list`` contains the parameters for each invocation of callable. Each item in ``args_list`` should be either a 2-item tuple of the list of positional arguments and a dictionary of keyword arguments or a single, non-tuple argument.<br>
`args_list`是一个列表，包含`callable`函数的参数，比如线程池中第一个`callable`会取`args_list[0]`作为参数，第二个`callable`会取`args_list[1]`作为参数，<br>
就是说，线程池中每个线程执行的函数是相同的，但是参数可以不同<br>
`args_list`列表可以有两种结构，<br>
* 第一种：<br>
每个元素是一个`tuple`，每个`tuple`中只能有两个元素，`tuple`中第一个元素是一个列表，按顺序存放`callable`中的参数，第二个元素是一个词典，通过关键字来索引`callable`的参数<br>
* 第二种：<br>
`args_list`中每个元素是单个的参数<br>

`callback`接收两个参数，一个是request，一个是result，result对应request中callable的返回值，如果没有返回值result是None<br>


`pool.putRequest(req)`:<br>
把运行多线程的函数放入线程池中<br>
`pool.wait()`:<br>等待所有的线程完成工作后退出<br>


#### multiprocessing

因为GIL（全局解释器锁）的限制（GIL是用来保证在任意时刻只能有一个控制线程在执行），所以python中的多线程并非真正的多线程。只有python程序是I/O密集型应用时，多线程才会对运行效率有显著提高（因在等待I/O的时，会释放GIL允许其他线程继续执行），而在计算密集型应用中，多线程并没有什么用处。考虑到要充分利用多核CPU的资源，允许python可以并行处理一些任务，这里就用到了python多进程编程了。multiprocessing是python中的多进程模块，使用这个模块可以方便地进行多进程应用程序开发。multiprocessing模块中提供了：Process、Pool、Queue、Manager等组件。<br>



### new import:<br>
`multiprocessing`:<br>
multiprocessing包是Python中的多进程管理包。与threading.Thread类似，它可以利用multiprocessing.Process对象来创建一个进程。该进程可以运行在Python程序内部编写的函数。该Process对象与Thread对象的用法相同，也有start(), run(), join()的方法。此外multiprocessing包中也有Lock/Event/Semaphore/Condition类 (这些对象可以像多线程那样，通过参数传递给各个进程)，用以同步进程，其用法与threading包中的同名类一致。所以，multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。<br>

但在使用这些共享API的时候，我们要注意以下几点:<br>

在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)。所以，有必要对每个Process对象调用join()方法 (实际上等同于wait)。对于多线程来说，由于只有一个进程，所以不存在此必要性。<br>
multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先考虑Pipe和Queue，避免使用Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源)。<br>
多进程应该避免共享资源。在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数。在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们可以通过共享内存和Manager的方法来共享资源。但这样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率。
Process.PID中保存有PID，如果进程还没有start()，则PID为None。<br>


### keyword & fct:<br>

不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用:<br>
* `Queue`
* `Pipe`:<br>
 管道函数返回的两个连接对象表示管道的两端。每个连接对象都有`send()`和`recv()`方法(包括其他)。<br>
 Pipe可以是单向(half-duplex)，也可以是双向(duplex)。我们通过mutiprocessing.Pipe(duplex=False)创建单向管道 (默认为双向)。一个进程从PIPE一端输入对象，然后被PIPE另一端的进程接收，单向管道只允许管道一端的进程输入，而双向管道则允许从两端输入。<br>
 注意，如果两个进程(或线程)试图同时读取或写入管道的同一端，那么管道中的数据可能会被损坏。当然，在同一时间使用不同管道的过程中不会出现损坏的风险<br>
* `Manager`:<br>
Python中进程间共享数据，处理基本的queue，pipe和value+array外，还提供了更高层次的封装。使用multiprocessing.Manager可以简单地使用这些高级接口。 <br>
Manager()返回的manager对象控制了一个server进程，此进程包含的python对象可以被其他的进程通过proxies来访问。从而达到多进程间数据通信且安全。
Manager支持的类型有list,dict,Namespace,Lock,RLock,Semaphore,BoundedSemaphore,Condition,Event,Queue,Value和Array。 <br>
* `Pool`:<br>
当使用Process类管理非常多（几十上百个）的进程时，就会显得比较繁琐，这是就可以使用Pool（进程池）来对进程进行统一管理。进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进程，有新进程请求执行时，就会被阻塞，直到池中有进程执行结束，新的进程请求才会被放入池中并执行。<br>
`pool.apply(self, func, args=(), kwds={})`:<br>阻塞型进程池，会阻塞主进程，直到工作进程全部退出，**一般不用这个**<br>
`apply_async(self, func, args=(), kwds={}, callback=None)`：<br>非阻塞型进程池 <br>


查询12306车票信息
---

### new import:<br>
`docopt`:<br>
命令行参数解析工具   [manual](http://docopt.org/)<br>
在代码的最开头使用 """ """文档注释的形式写出符合要求的文档，就会自动生成对应的字典<br>
`re`:<br>正则表达式<br>
`pprint`:<br>美观地打印打印 Python 数据结构<br>   [manual](https://docs.python.org/3/library/pprint.html)
`colorama`
`prettytable`

### keyword & fct:<br>
`__doc__`:<br>每个对象都会有一个__doc__属性，函数语句中，如果第一个表达式是一个string，这个函数的__doc__就是这个string，否则__doc__是None

#### 将list里面的unicode显示为中文
```python
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
stations = str(stations).replace('u\'','\'')
stations = stations.decode("unicode-escape")
```
`decode("unicode-escape")`:<br>
```python
str1 = '\u4f60\u597d'  
print str1.decode('unicode_escape')  
你好
```
字符串内容是unicode码，decode('unicode_escape')后将其转为对应的字符


pytohn编码 utf8 gbk

#### 对字典排序
使用[`sorted(iterable,key,reverse)`](#jump)<br>






















