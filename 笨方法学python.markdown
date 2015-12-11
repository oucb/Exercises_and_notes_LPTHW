# 笨方法学python

标签（空格分隔）： book

---

###ex32:循环和列表
**1.函数range()的使用**
``` python
>>> range(1,5) #代表从1到5(不包含5)
[1, 2, 3, 4]
>>> range(1,5,2) #代表从1到5，间隔2(不包含5)
[1, 3]
>>> range(5) #代表从0到5(不包含5)
[0, 1, 2, 3, 4]

#list操作
array = [1, 2, 5, 3, 6, 8, 4]
#其实这里的顺序标识是
[1, 2, 5, 3, 6, 8, 4]
(0，1，2，3，4，5，6)
(-7,-6,-5,-4,-3,-2,-1)

>>> array[0:] #列出0以后的
[1, 2, 5, 3, 6, 8, 4]
>>> array[1:] #列出1以后的
[2, 5, 3, 6, 8, 4]
>>> array[:-1] #列出-1之前的
[1, 2, 5, 3, 6, 8]
>>> array[3:-3] #列出3到-3之间的
[3]

#range中的[::]
>>> array[::2]
[1, 5, 6, 4]
>>> array[2::]
[5, 3, 6, 8, 4]
>>> array[::3]
[1, 3, 4]
>>> array[::4]
[1, 6] 
如果想让他们颠倒形成reverse函数的效果
>>> array[::-1]
[4, 8, 6, 3, 5, 2, 1]
>>> array[::-2]
[4, 6, 5, 1]
```
**2.apppend()函数的使用，列表的其它操作**
> * append()向列表尾部添加一个新的元素。只接受一个参数
* extend()只接受一个列表作为参数，将参数中的每个元素都添加到原列表
```
append()用法示例：
>>> mylist = [1,2,0,'abc']
>>> mylist
[1, 2, 0, 'abc']
>>> mylist.append(4)
>>> mylist
[1, 2, 0, 'abc', 4]
>>> mylist.append('haha')
>>> mylist
[1, 2, 0, 'abc', 4, 'haha']
extend()用法示例:
>>> mylist
[1, 2, 0, 'abc', 4, 'haha']
>>> mylist.extend(['lulu'])
>>> mylist
[1, 2, 0, 'abc', 4, 'haha', 'lulu']
>>> mylist.extend(['123123','lalalala'])
>>> mylist
[1, 2, 0, 'abc', 4, 'haha', 'lulu', '123123', 'lalalala']
>>> mylist.extend([111111,222])
>>> mylist
[1, 2, 0, 'abc', 4, 'haha', 'lulu', '123123', 'lalalala', 111111, 222]
```

###ex33:while循环
**1.while-loop会一直执行它下面的代码片段，直到它对应的布尔表达式为false时停止**
**2.while循环有时候会永不结束，因此：**
> * 尽量少用while-loop,for-loop会是更好的选择
* 重复检查while语句，确定测试的布尔表达式最终会变成false
* 若不确定，在while-loop的结尾打印出要测试的值，观察其变化

###ex34:访问列表的元素
1.序数(orginal number)与基数(cardinal number)区别
> 
ordinal == 有序，以1开始;cardinal == 随即选取，以0开始

2.序数与基数概念
> 在日常交流中，基数或量数是对应量词的“数”，例如在以下句子中的“一”及“四”：“有一个橙，有四个柑”。序数是对应排列的“数”，例如在以下句子中的“（第）一”及“（第）二”：“这人一不会打字，二不懂速记，所以不可以做秘书”；“第二个人正在进来”。

###ex35:分支和函数

###ex36:设计和调试
**1.if语句的规则**
> * 每一个“if语句”必须包含一个else
* 如果这个else永远都不应该被执行，即它本身没有任何意义，则必须在else语句后面使用
一个叫做die的函数，以打印错误信息并且死给你看
* "if语句“的嵌套不要超过2层，最好尽量保持只有一层。即若if里边又有了一个if，需把第二个if移到另一个函数
* 将”if语句“当成段落来对待，其中的每一个if，elif，else组合就跟一个段落的句子组合一样。在这种组合的最前面和最后面留一个空行以作区分。
* 你的不二测试应该很简单，如果他们很复杂的话，你需要将他们的运算事先放到一个变量里，并且为变量取一个名字。

**2.循环的规则**
> * 只有当循环永不停止时使用“while循环”，这意味着你可能永远都用不到。这条只有python中成立，其他的语言另当别论。
* 其他类型的循环都使用“for循环”，尤其是在循环的对象数量固定或者有限的情况下

**3.调试(debug)的小技巧**
> * 不要使用“debugger”。Debugger所作的相当于对病人的全身扫描。你并不会得到某方面的有用信息，而且你会发现它输出的信息态度，而且大部分没有用，或者只会让你更困惑。
* 最好的调试程序的方法是使用print在各个你想要检查的检查的关键环节将关键变量打印出来，从而检查哪里是否有错。
* 让程序一部分一部分地运行起来。不要等一个很长的脚本写完后才去运行它。写一点，运行一点，再修改一点。

###ex39:列表的操作
**1.mystuff.append('hello')**
>* 查找变量mystuff
* 一旦找到mystuff，就处理句点.操作符，同时查看mystuff内部的一些变量。由于mystuff是一个列表，python知道mystuff支持的一些函数
* 接下来处理append。python会将“append”和mystuff支持的所有函数的名称一一对比，如果有append这个函数，那就会去使用这个函数
* 接下来看到括号并意识到这应该是一个函数，到这它就会正常调用这个函数，不过这里的函数还要多一个参数才行
* 这个额外的参数其实是...mystuff！真正发生的事情其实是append(mystuff,'hello'),不过你看到的只是mystuff.append('hello')

**2.split()**
```python
the syntax for split() method:string.split(str=' ',num=string.count(str))
# using str as the delimiter string to separate the string and num is the times of separator,return a list of strings
>a = "boys and girls"
>print a.split(' ')
>["boys", "and", "girls"]
>a = "boys_and_girls"
>print a.split('_')
>["boys", "and", "girls"]
```
**3.pop()**
```python
the syntax for pop() method:list.pop(obj=list[-1])
# remove obj from the list(last as the default) and return it
>a = ["one", "two", "three"]
>print a.pop()
>three
>print a.pop(1)
>"two"
```
**4.join()**
```python
the syntax for join() method:str.join(sequence)
#join the string elements of the list sequence by the str separator and return it
>a = ["oh!", "my", "God"]
>s = " "
>print s.join(a)
>oh! my God
>print s.join(a[1:])
>my God
```

**习题1和习题2**
```python
1.ten_things.split(' ') :split(ten_things,' ')
#用’ ‘分割(split)ten_things,为ten_things和’ ‘调用split函数
2.more_stuff.pop()      :pop(more_stuff)
#移除(pop)more_stuff最后一个元素，为more_stuff调用pop函数
3.stuff.append(next_one):append(stuff,next_one)
#将next_one加入(append)stuff，为stuff和next_one调用append函数
4.stuff.pop()           :pop(stuff)
#同more_stuff.pop()
5.' '.join(stuff)       :join(' ',stuff)
#用’ ‘连接(join)stuff,为’ ‘和stuff调用join函数
6.'#'.join(stuff[3:5])  :join('#',stuff[3:5])
#用’#‘连接(join)stuff[3:5],为’#‘和stuff[3:5]调用join函数
```

###ex40:字典，可爱的字典
```python
# the find_city is a function
cities['_find'] = find_city
city_found = cities['_find'](cities, state)
# it's means that the dict can index to a function
```
**习题1.functions that dict can call**
```python
1.items()
# return a copy of the dictionary's list of (key, value) pairs.
2.keys()
# return a copy of the dictionary's list of keys.
3.valuse()
# return a copy of the dictionary's list of values.
4.viewitems、viewkeys()、viewvalues()
# return a new view of the dictionary's ~.
```
**习题2**

* 是随机无序的
* 不能被for-loop调用
* key与value不能相互索引

**习题3**

* dict无法执行for-loop，在dict调用items()返回值dict上调用for-loop将返回dict的(key,value)对

###ex41:来自Percal 25号行星的哥顿人（Gothons）
**习题1**
set the return value to next,retrieving from the dict ROOMS for the key next and set the index value to room,running the function of the room().the next is a variable to receive the key of functions and the room is to receive the functions.
**习题2**

###ex42:物以类聚
**1.Class(类)**
> * 这里我们把其当作高级的“函数字典”使用。
* 用到“class”的编程语言被称作“Object Oriented Programming(面向对象编程)"

**2.getattr&setattr**
```python
getattr(object, name, default)
# get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
# when a default argument is given, it is returned when the attribute doesn't exit;
# without it, an exception is raised in that case.
```
**3.私有变量**
以__开头，不以__结尾的变量

**习题.1**
一个实例的__dict__属性仅仅是那个实例的局部属性集合，dir()用来获取一个对象的所有有效属性。（__slots__）
```python
>>>class Foo(object):
    __slots__ = ('bar', )
    bar = 'spam'
>>>Foo.__dict__
#显示类属性
>>>Foo().__dict__
#提示错误：由于使用了slots，故类的实例将不会拥有__dict__属性。
```
**习题.2**

###ex45:对象、类、以及从属关系
类是一个用来描述具有同类属性的实例的概括性的总称

**1.“is-a(是啥)"和”has-a(有啥)"**
"是啥“要用在谈论”两者以类的关系互相关联“的时候，而”有啥“要用在”两者无共同点，仅
是互为参照“的时候。

**习题1."object"类**
py2的新式类，object是一个较新的基类，继承了object的类都是new style class，由于他们都是object的派生类，便于统一操作，没有继承的为classic class。
```python
class Foo(object):
    pass

class Foo1:
    pass

print type(Foo), type(Foo1)
print dir(Foo)
print dir(Foo1)
print isinstance(Foo, object)
print isinstance(Foo1, object)
```
```python
<type 'type'> <type 'classobj'>
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__doc__', '__module__']
True
True
```
**习题.2**
类继承

**习题.3**
当函数在Animal这样的“基类(base class)”里时，Fish和Dog等子类的对象实例都可调用它；当在Dog时，只有Dog的对象实例可以调用。

###ex46:一个项目骨架
**1.项目骨架**
以一个名称为NAME的项目为例：
>* NAME项目主文件夹，存放项目文件，包含`__init__.py`文件
* bin文件夹，存放可执行python脚本
* docs文件夹，存放项目文档
* tests文件夹，存放测试文件，包含`__init__.py`和NAME_tests.py
* setup.py文件，项目概括信息

**2.setup.py**
1.执行python setup.py sdist会为模块创建一个源码包。
>在当前目录下创建dist目录，里面有个分发包文件xxx-1.0.tar.gz

2.在xxx-1.0.tar.gz解压目录下执行python setup.py install
>会将xx.py拷贝到python类路径下，可被导入使用，若是egg文件，则会拷贝到dist-packages目录下

3.生成相关格式文件
>windows下执行python setup.py bdist_wininst生成一个exe文件；linux下执行python setup.py bdist_rpm生成rpm包，但系统必须有rpm命令的支持，执行python setup.py bdist --help-formats查看所有格式的支持

4.setup函数的一些参数
>* packages
告诉Distutils需要处理那些包（包含`__init__.py`的文件夹）
* package_dir
告诉Distutils哪些目录下的文件被映射到哪个源码包，感觉好像是一个相对路径的定义。一个例子：package_dir = {'': 'lib'}，表示以lib为主目录。
* ext_modules
是一个包含Extension实例的列表，Extension的定义也有一些参数。
* ext_package
定义extension的相对路径
* requires
定义依赖哪些模块
* provides
定义可以为哪些模块提供依赖
* scripts
指定python源码文件，可以从命令行执行。在安装时指定--install-script
* package_data
通常包含与包实现相关的一些数据文件或类似于readme的文件。
`package_data = {'': ['*.txt'], 'mypkg': ['data/*.dat'],}`
表示包含所有目录下得txt文件和mypkg/data目录下的所有dat文件
* data_files
指定其他的一些文件（如配置文件）


**3.nose使用**
nose extends the test loading and running features of unittest, making it easier to write, find and run tests.By default, nose will run tests in files or directories under the current working directory whose names include “test” or “Test” at a word boundary (like “test_this” or “functional_test” or “TestClass” but not “libtest”). 
>* 路径、模块（文件）、类、函数的名字如果能和testMatch正则表达式匹配上，那就会被认为是一个用例
* 测试用例的命名需以test_开头
* 在tests目录的上一层执行测试命令nosetests
* setup和teardown
setup:在测试用例开始时被执行
teardown:在测试用例结束后被执行

**4.virtualenv**
virtualenv is a tool to create isolated Python environments.
1.创建**ENV**的虚拟环境
```shell
virtualenv ENV
virtualenv --no-site-package '虚拟环境名称‘    （创建的虚拟环境不依赖系统环境中的site packages）
```
2.启动
```shell
cd ENV
source ./bin/activate
```
3.退出
```shell
deactivate
```
4.virtualenvwrapper
virtualenv的扩展包，用于方便管理虚拟环境


###ex47：自动化测试
**1.nosetest以及其它测试**

**2.doc tests**

###ex48:更复杂的用户输入
**1.元组**
tuple是一个不能修改的列表，成员之间需要用逗号隔开，方括号换成圆括号()
tuple_test = ('first', 'second')
**2.异常**
异常(exceptions)指的是你运行某个函数时得到的错误。你的函数碰到错误时，就会“提出(raise)”一个“异常”，然后你就要去处理(handle)这个异常。
**3.处理异常**
处理(handle)异常我们使用try和except这两个关键字：
```python
def convert_number(s):
try:
    return int(s)
except ValueError:
    return None
```
其中运行代码放到try的区段里，出错后要运行的代码放到except区段里。
###ex49：创建句子
**1.assert_raises使用**
文档如下
```
assert_raises = assertRaises(self, excClass, callableObj=<function _sentinel>, *args, **kwargs) method of nose.tools.trivial.Dummy instance
        Fail unless an exception of class excClass is raised
        by callableObj when invoked with arguments args and keyword
        arguments kwargs. If a different type of exception is
        raised, it will not be caught, and the test case will be
        deemed to have suffered an error, exactly as for an
        unexpected exception.
        
        If called with callableObj omitted, will return a
        context object used like this::
        
             with self.assertRaises(SomeException):
                 do_something()
        
        The context manager keeps a reference to the exception as
        the 'exception' attribute. This allows you to inspect the
        exception after the assertion::
        
            with self.assertRaises(SomeException) as cm:
                do_something()
            the_exception = cm.exception
            self.assertEqual(the_exception.error_code, 3)
```
>assert_raises(excClass, callableObj=<function _sentinel>, *args, **kwarts)

**excClass是抛出错误的class名，callableObj为测试函数名，*args为传递给测试函数的参数**




























