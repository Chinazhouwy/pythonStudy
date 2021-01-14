#!/usr/bin/python3
print("Hello, World!")
...
type(...)
print(...)
print(type(...))
print(Ellipsis)
print(bool(...))
# id()
# id() 函数返回对象的唯一标识符，标识符是一个整数。
# CPython 中 id() 函数用于获取对象的内存地址。
print(id(...))
print(id(...))
print(id(Ellipsis))
print(id(Ellipsis))
print(id(type(Ellipsis)))

#它是 Numpy 的一个语法糖
#在 Python 3 中可以使用 … 代替 pass
def func01():
    ...

func01()