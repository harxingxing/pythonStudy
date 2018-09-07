# !/user/local/python3/bin
"""
document notes
"""

'''
# 列表
'''
# list = [1, 2]
# list.append(3)  # [1, 2, 3]
# list.extend([3, 4])  # [1, 2, 3, 4]
# list.insert(0, 3)  # [3, 1, 2]
# list.remove(2)  # [1] 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误
# list.pop(1) # [1] 参数为下标，为空默认移除最后一个元素
# list.clear(); # [] 移除列表中的所有项，等于del a[:]。
# key = list.index(2); print(a) # 1  返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
# count = list.count(1); print(count) # 1 返回 x 在列表中出现的次数。
# list.sort()
# list.reverse() # [2, 1] 倒排列表中的元素。倒排，不是倒序
# copylist = list.copy(); print(copylist) #　[1, 2]
# print(list)

'''
#! 列表推导式
'''
# vec = [2, 4, 6]
# str = [3 * x for x in vec]
# print(str)  # [6, 12, 18]
## 对序列里每一个元素逐个调用某方法
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# str = [weapon.strip() for weapon in freshfruit]
# print(str)  # ['banana', 'loganberry', 'passion fruit']
# vec = [2, 4, 6]
# str = [3 * x for x in vec if x > 3]
# print(str)  # [12, 18]

'''
#! todo:嵌套列表解析
'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matrix2 = [
    [row for row in matrix]
    # for i in range(4)
]
print(matrix2)

'''
# 元组和序列
元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。
'''
# t = 12345, 54321, 'hello!'
# u = t, (1, 2, 3, 4, 5)
# print(t[0])  # 12345
# print(t) # (12345, 54321, 'hello!')
# print(u) # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

'''
# 字典
'''
# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对
# dict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(dict)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
# dict = dict(sape=4139, guido=4127, jack=4098)
# print(dict)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}

'''
# 遍历技巧

'''
## 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)
## gallahad the pure
## robin the brave

## 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)
## 0 tic
## 1 tac
## 2 toe

## 同时遍历两个或更多的序列，可以使用 zip() 组合
##! {0}{1}{2}是指第几个，以0指当前第一个列表的当前元素
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# answers2 = [1, 2, 3]
# for q, a, a2 in zip(questions, answers, answers2):
#     print('What is your {0}?  It is {1}{2}.'.format(q, a, a2))
## What is your name?  It is lancelot.
## What is your quest?  It is the holy grail.
## What is your favorite color?  It is blue.
