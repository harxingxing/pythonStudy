# !/usr/local/python3/bin
"""
document note:
"""

'''
# Python3 编程第一步
右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。
关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
'''
# a, b = 0, 1
# while b < 1000:
#     print(b, end='')
#     a, b = b, a + b

'''
# if 语句
每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
在Python中没有switch – case语句。
if像其他语言一样，可以嵌套
'''
# if False:
#     statement_block_1 = 1
# elif False:
#     statement_block_2 = 1
# else:
#     statement_block_3 = 3

'''
# while 循环 和 while 循环使用 else 语句
同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中

'''
# i = 1;
# while i < 3:
#     print(i)
#     i += 1

## while 循环使用 else 语句
# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")

'''
# for 语句
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

'''
todo:
# break和continue语句及循环中的else子句
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环
    被break终止时不执行。
'''
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')

'''
#　pass 语句
pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句
'''
# while True:
#     pass

'''
# 迭代器
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器
'''
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print (next(it))   # 输出迭代器的下一个元素

'''
# !生成器
使用了 yield 的函数被称为生成器（generator）。
调用一个生成器函数，返回的是设定的那个迭代器对象。生成器就是一个迭代器。
'''
# import sys
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

'''
#　定义一个函数
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
def 函数名（参数1, 参数2, ...）:
    函数体
'''
## 计算面积函数
# def area(width, height):
#     return width * height
# print(area(10, 20))

'''
# 可更改(mutable)与不可更改(immutable)对象
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
    比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la
    也会受影响。
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''

'''
# 参数
必需参数：须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
关键字参数：使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
默认参数：调用函数时，如果没有传递参数，则会使用默认参数。
不定长参数：你可能需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数。
    def functionname([formal_args,] *var_args_tuple ):
       "函数_文档字符串"
       function_suite
       return [expression]
    加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。

'''
# # 关键字参数，这里关键字为str
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
# # 调用printme函数
# printme(str="菜鸟教程")

'''
# 匿名函数
使用 lambda 来创建匿名函数。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运
    行效率。
lambda 函数的语法只包含一个语句
    lambda [arg1 [,arg2,.....argn]]:expression
'''
# ## 匿名函数实例
# sum = lambda arg1, arg2: arg1 + arg2
# ## 调用sum函数
# print("相加后的值为 : ", sum(10, 20))

'''
# 变量作用域
Python的作用域一共有4种
    L （Local） 局部作用域
    E （Enclosing） 闭包函数外的函数中
    G （Global） 全局作用域
    B （Built-in） 内建作用域
'''
# x = int(2.9)  # 内建作用域
# g_count = 0  # 全局作用域
# def outer():
#     o_count = 1  # 闭包函数外的函数中
#     def inner():
#         i_count = 2  # 局部作用域

## Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、
##   try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问。
## 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
# if True:
#     msg = 'I am Bob.'
# print(msg)

'''
# global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
'''
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num)
#     num = 123
#     print(num)
# fun1()

## 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了。
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()

## 另外有一种特殊情况，假设下面这段代码被运行：
# a = 10
# def test():
#     a = a + 1  # 错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改。
#     print(a)
# test()
