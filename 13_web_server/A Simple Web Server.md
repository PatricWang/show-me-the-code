A Simple Web Server
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

使用socket编写聊天工具
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
