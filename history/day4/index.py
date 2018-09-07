# !/usr/local/python3/bin
"""
document notes
"""
'''
# 模块
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。
模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。

1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
2、sys.argv 是一个包含命令行参数的列表。
3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
'''
## 文件名: using_sys.py
# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#     print(i)
# print('\n\nPython 路径为：', sys.path, '\n')

'''
# import 语句
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
import module1[, module2[,... moduleN]
当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端。
一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量。
'''
## 引入 support 模块：
# # 导入模块
# import support
# # 现在可以调用模块里包含的函数了
# support.print_func("Runoob")

## 验证在路径下的包可以直接被导入
# >>>import fibo
# >>>fibo.fib(1000)
# >>>fibo.fib2(100)
# >>>fibo.__name__
# # 如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：
# >>> fib = fibo.fib
# >>> fib(500)

'''
# from…import 语句
Python的from语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：from modname import name1[, name2
    [, ... nameN]]
>>> from fibo import fib, fib2 这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引
    入进来。
'''

'''
# From…import* 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：from modname import *
这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。大多数情况， Python程序员不使用这种
    方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。
'''

'''
# __name__属性
如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
'''
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')
# import support

'''
# dir() 函数
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
'''
# import fibo, sys
# print(dir(fibo))
# print(dir(sys))
# # 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
# print(dir())

'''
# 包
包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不
    小心的影响搜索路径中的有效模块。
'''

'''
# 从一个包中导入*
我们使用 from sound.effects import *,Python 会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都
    导入进来。但是很不幸，这个方法在 Windows平台上工作的就不是非常好，因为Windows是一个大小写不区分的系统。
导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在
    使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
作为包的作者，可别忘了在更新包之后保证 __all__ 也更新了啊。
'''