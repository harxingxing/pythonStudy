## 第一部分：基础语法
# !/usr/bin/python3

## 输出hello，World!
# print('Hello, World!')

## 输出保留关键字
# import keyword
# print(keyword.kwlist)

## 缩进实例
# if True:
#     print('True')#前面空格必须一致
#     print('True2')#前面空格必须一致
# else:
#     print('False')
#  print('heihei')# 缩进不一致，会导致运行错误

## 多行语句
## Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
# one = 1
# two = 2
# three = 3
# total = one + \
#         two + \
#         three
# # 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
# array = [one, two,
#          three]

# # 多行字符串
# longString = '''
# 我是可以
# 换行的
# 一个字符串
# '''
# print(longString)

# str = 'Runoob'
# print(str[0:-1])# 输出第一个到倒数第二个的所有字符
# print(str[0]) # 输出字符串第一个字符
# print(str[2:]) # 输出从第三个开始的后的所有字符
# print(str * 3) # 输出字符串两次
# print(str + '你好') # 连接字符串
# print('hello\nrunoob')# 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')# 在字符串前面添加一个 r，表示原始字符串，不会发生转义

## 等待用户输入
# input("\n\n按下enter健后退出")

## 一行多条语句
# import sys;x = 'runoob';sys.stdout.write(x + '\n');

## print不换行输出
# x = 'a';
# print(x)
# print(x, end='')

## 导入 sys 模块
# import sys
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

## 导入 sys 模块的 argv,path 成员
# from sys import argv, path  # 导入特定的成员
# print('================python from import===================================')
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

## 打印输出一个函数的文档字符串
# help(max)

'''
知识点：
默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 为源码文件指定不同的编码格式为：
    -*- coding:编码 -*-
标识符对大小写敏感，在 Python 3 中，非 ASCII 标识符也是允许的了
单行注释使用#，多行如编写当前注释一样(编写文档信息建议使用双引号)
python是使用缩进来表示代码块，不需要使用大括号 {} ，缩进的空格数是可变的，但是同一个代码块的语句必须包含相同
    的缩进空格数
python中单引号和双引号使用完全相同
使用三引号(\'''或""")可以指定一个多行字符串
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
字符串的截取的语法格式如下：变量[头下标:尾下标]
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开
    始。空行与代码缩进不同，空行并不是Python语法的一部分。作用在于分隔两段不同功能或含义的代码，便于日后代码
    的维护或重构
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *

在 Windows 下可以不写第一行注释:#!/usr/bin/python3
调用 python 的 help() 函数可以打印输出一个函数的文档字符串,如下实例，查看 max 内置函数的参数列表和规范的
   文档>>> help(max)

概念：
数字(Number)类型：包括整数、布尔型、浮点数和复数
代码组:缩进相同的一组语句构成一个代码块
子句(clause):像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行
    代码构成代码组。我们将首行及后面的代码组称为一个子句(clause)。
'''

## 第二部分：基本数据类型
## 多个变量赋值
# a,b,c = 1,2,'runoob'

## 删除多个对象
# var1 = 1
# var2 = 2
# print(var1)
# print(var2)
# del var1, var2
# print(var1)# 因为不存在，所以会报错

## 数值运算的几种特殊情况
# print(2**5)# 乘方

## 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
# tup1 = ()    # 空元组
# tup2 = (20,) # 一个元素，需要在元素后添加逗号

## 创建集合
# parame = {'value1', 'value2'}
# parame2 = set('value')
# print(parame2)

# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)  # 输出集合，重复的元素被自动去掉
## 成员测试
# if ('Rose' in student):
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')

## set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(b)
# print(a - b)  # a和b的差集
# print(a | b)  # a和b的并集
# print(a & b)  # a和b的交集
# print(a ^ b)  # a和b中不同时存在的元素

## 字典实例
# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
# tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
#
# print(dict['one'])
# print(dict[2])
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值

## 个人总结（小结）

'''
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。p.基本数据类型
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。p.基本数据类型
Python3 中有六个标准的数据类型:
    不可变数据（四个）：Number（数字）、String（字符串）、Tuple（元组）、Sets（集合）；
    可变数据（两个）：List（列表）、Dictionary（字典）。p.标准数据类型
todo:isinstance 和 type 的区别?p.Number（数字）
del语句删除一些对象引用,语法：del var1, var2。p.Number（数字）
数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。在混合计算时，Python会把整型转换成为
    浮点数。p.数值运算
Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮
    点型。p.数值运算
索引值以 0 为开始值，-1 为从末尾的开始位置。加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数
    字为复制的次数。p.String（字符串）
List（列表）：与php数组类似，只是输出方式不太一样,与Python字符串不一样的是，列表中的元素是可以改变的。p.List（列表）
Tuple（元组）：元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号
    隔开。p.Tuple（元组）
集合（set）：是一个无序不重复元素的序列。基本功能是进行成员关系测试和删除重复元素。可以使用大括号 { } 
    或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
Dictionary（字典）：列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来
    存取的，而不是通过偏移存取。在同一个字典中，键(key)必须是唯一的。p.Dictionary（字典）


总结：
几种类型之间的区别：查看：http://note.youdao.com/noteshare?id=2e5b0c3c191f43164ed8f8a92e49e110&sub=757E0C25DE1544DE85BC3609FB3EC173


'''
