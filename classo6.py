'''
第6课：模块和包
在Python中，模块是包含Python定义和声明的文件。一个模块可以包含函数、类、变量和运行代码。通过模块，Python支持程序的模块化，这是代码重用的关键。包是一种封装多个模块的方式，通常使用文件夹来组织。

导入标准库模块
Python自带了一个标准库，可以通过import语句导入这些库中的模块。例如，math模块提供了数学相关的函数。

python
Copy code
import math

result = math.sqrt(25)
print(result)  # 输出5.0
安装和使用第三方包
除了标准库，你还可以使用pip（Python的包安装程序）来安装第三方包。这些包通常在PyPI（Python Package Index）中注册。

bash
Copy code
pip install requests
然后，你可以在你的程序中导入和使用这个包。

python
Copy code
import requests

response = requests.get('https://www.python.org')
print(response.text)  # 输出网页的HTML内容
创建自己的模块
创建自己的模块很简单，只需要将相关的函数和变量保存在一个.py文件中。例如，创建一个名为mymodule.py的文件，并定义一些函数。

python
Copy code
# mymodule.py

def greeting(name):
    print(f"Hello, {name}")
然后你可以在另一个Python脚本中导入并使用这个模块。

python
Copy code
import mymodule

mymodule.greeting('Alice')  # 输出 "Hello, Alice"
课后练习题
尝试导入Python的random模块，并使用它生成一个随机数。
安装第三方包（如果你的环境允许），例如requests，并试着发送一个GET请求到一个网站。
创建自己的模块，包含一些函数，然后在另一个文件中导入并使用这些函数。
通过完成这些练习，你将学会如何利用模块来组织代码，以及如何使用标准库和第三方库来扩展Python的功能。模块和包是Python编程中非常重要的组成部分，它们使得代码更加模块化和可重用。
'''