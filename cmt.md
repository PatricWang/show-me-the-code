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

###import:<br>
sklearn
[sklearn reference](http://scikit-learn.org/stable/index.html)  [中文](http://sklearn.apachecn.org/cn/stable/index.html)

###key word&fct:<br>
`open`:打开文件<br>
`with-as`:适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等
`read()`:读所有内容，放到字符串中<br>
`readline()`:读一行,<br>
`readlines()`:读所有内容，生成一个行的列表(list)，可以用for...in处理
`numpy.sum`:返回类型为`numpy.ndarray`
`sorted`:<br>
**sort 与 sorted 区别:<br>**
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。<br>
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。<br>
sorted(iterable, cmp=None, key=None, reverse=False)<br>
1.cmp，比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0<br>
2.key，主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序<br>
3.reverse，是否反转，默认情况下不反转<br>
`zip`:

###other:<br>
字符串前加r，防止字符转义
字符串前加u，unicode字符串

[稀疏矩阵csr_matrix](https://app.yinxiang.com/shard/s72/nl/17217582/4de137bc-df5d-45ce-a735-0c53b89aec0a)
[numpy.sum(axis=0)解释](https://segmentfault.com/q/1010000010111006/a-1020000010131823):<br>
简单说对于二维数组，axis=0 按列相加，axis=1 按行相加，详细解释看上面链接


