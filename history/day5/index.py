# !/usr/local/python3/bin
"""
document notes
"""
'''
# Python3 输入和输出
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
'''
# s = 'Hello, Runoob'
# print(str(s))
# print(repr(str(s)))

## repr() 函数可以转义字符串中的特殊字符
# hello = 'hello, runoob\n'
# hellos = repr(hello)
# print(hellos)
## # repr() 的参数可以是 Python 的任何对象
# repr((x, y, ('Google', 'Runoob')))

## 函数的使用
##rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。还有类似的方法, 如 ljust() 和 center()。

## Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
# print('12'.zfill(5))
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(5))

## format()，括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
# print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
## 在括号中的数字用于指向传入对象在 format() 中的位置
# print('{0} 和 {1}'.format('Google', 'Runoob'))
# print('{1} 和 {0}'.format('Google', 'Runoob'))

## 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
# print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

## 位置及关键字参数可以任意的结合
# print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

##! '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
# import math
# print('常量 PI 的值近似为： {}。'.format(math.pi))
# print('常量 PI 的值近似为： {!r}。'.format(math.pi))

## 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。
