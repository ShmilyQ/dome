# 练习题 1: 扩展类（Class）
# 🔹 任务：创建一个名为 Book 的类，包含属性：书名（title）、作者（author）和页数（pages）。此外，添加一个方法 description，当调用时，它返回书籍的详细信息。

class Book :

    def __init__(self, title, author, pages) :

        self.title = title
        self.author = author
        self.pages = pages

    def description(self) :

        return f'\n书籍名称：{self.title}     作者：{self.author}     页数：{self.pages}\n'
    
book = Book('三国演义','罗贯中','9999')
print(book.description())



# 练习题 2: 创建和使用自定义模块
# 🔹 任务：创建一个名为 utilities.py 的模块，该模块包含两个函数：一个用于计算两个数字的和，另一个用于计算两个数字的差。然后，在另一个文件中导入这个模块并使用这些函数。

from utilities import *

uti = utilities(10,20)

print(f'两数之和为：{uti.sum()}\t两数只差为：{uti.num()}\n')

# 练习题 3: 文件读写
# 🔹 任务：编写一个程序来创建一个名为 diary.txt 的文件，并写入一些日记条目。然后，编写另一部分代码来读取并打印这个文件的内容。

import datetime

with open('diary.txt','w') as file :

    st = input('请输入一串字符：')

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    file.write(f'[{time} 插入一条数据]：{st}\n')

with open('diary.txt','r') as file :

    con = file.read()

    print(con)

# 练习题 4: 处理异常
# 🔹 任务：修改练习题 3 中的程序，添加异常处理来处理可能出现的 FileNotFoundError。如果文件不存在，程序应输出一条友好的错误消息，而不是抛出异常。


import datetime

try :
    with open('diary.txt','w') as file :

        st = input('请输入一串字符：')

        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        file.write(f'[{time} 插入一条数据]：{st}\n')
except FileExistsError:

    print('文件写入失败！')

try :
    
    with open('diary.txt','r') as file :

        con = file.read()

        print(con)

except FileNotFoundError:

    print('文件打开失败，请检查文件是否存在或文件路径是否正确！')