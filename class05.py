'''
第5课：函数
在Python中，函数是组织好的，可重复使用的，用来实现单一或关联功能的代码段。函数可以提高应用的模块性和代码的重用率。

定义函数
在Python中，使用def关键字来定义函数，后跟一个函数的名称和圆括号()，其中可以包含一些参数。

python
Copy code
def greet(name):
    """这是一个打招呼的函数"""
    print(f"Hello, {name}!")
参数与返回值
函数可以接受参数，这些参数可以在函数内部使用。函数也可以返回值，用return语句来实现。

python
Copy code
def add(a, b):
    """这是一个加法函数"""
    return a + b
文档字符串（docstrings）
文档字符串（docstrings）是一个重要的特性，它提供了一种方便的方法来为函数、模块和类编写文档。

python
Copy code
def multiply(a, b):
    """返回两个数的乘积。
    参数：
    a -- 第一个数
    b -- 第二个数
    """
    return a * b
作用域
在Python中，变量有不同的作用域：局部作用域、外围作用域、全局作用域和内建作用域。变量的作用域取决于它在代码中的位置。

python
Copy code
x = 'global'

def function_scope():
    x = 'local'
    print(x)

function_scope()  # 输出 'local'
print(x)  # 输出 'global'
'''

# 课后练习题
# 创建一个函数，它接受一个参数并打印出该参数的值。

def test(x) :

    return print(f'\nhello {x}\n')
    
test('Jack')

# 编写一个函数，它接受两个参数并返回它们的和。

def sum(a, b) :

    return a + b

print(f'a + b = {sum(10, 20)}\n')

# 编写一个带有文档字符串的函数，该函数接受两个参数并返回它们的乘积。使用help()函数来查看文档字符串。

def product(s, n) :

    """计算s乘以n的值"""

    return s * n

print(f's * n = {product(10, 2)}\n')
help(product)

# 尝试理解局部变量和全局变量的区别，并编写一个示例函数来说明这一点。

x = 10

def num() :

    x = 33
    print(f'x = {x}')

print(f'x = {x}')

num()