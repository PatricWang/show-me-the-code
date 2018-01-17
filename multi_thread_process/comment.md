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
