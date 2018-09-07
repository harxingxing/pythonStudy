# !/usr/local/python3/bin
## 如果这里注释掉，index.py就回出错
def print_func(par):
    print("Hello : ", par)
    return

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')