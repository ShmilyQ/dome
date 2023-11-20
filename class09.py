'''
1. 高级数据结构
集合（Sets）：了解集合的基本操作，如创建集合、添加元素、集合运算（交集、并集、差集）。
字典的高级应用：深入探索字典，包括字典推导式、嵌套字典，以及如何有效地使用字典。

2. 列表、字典和集合推导式
探索Python的推导式（comprehensions），这是一种简洁、高效创建数据结构的方法。

3. 函数的高级特性
参数类型：深入了解不同类型的参数，如位置参数、关键字参数、默认参数。
可变参数：学习如何定义接受任意数量参数的函数。
Lambda函数：探索匿名函数的使用及其在编程中的应用。

4. 模块和包
创建和使用包：了解如何组织模块成包，以及如何导入和使用包中的模块。

5. 文件和异常处理的高级应用
读写不同类型的文件：了解如何处理不同类型的文件，如CSV、JSON等。
上下文管理器：深入理解 with 语句的原理和用法。
高级异常处理：学习更复杂的异常处理技术，如创建自定义异常。


'''

my_set = set()

set = {'set1','set2','set3'}
set1 = {'set4','set5','set6'}

# 并集 - 包含set1和set2的所有元素
union_set = set.union(set1)

print(union_set)

# 交集 - 同时包含于set1和set2的元素
intersection_set = set.intersection(set1)

print(intersection_set)

# 差集 - 包含于set1但不包含于set2的元素
difference_set = set.difference(set1)

print(difference_set)

# 创建一个字典，键为1到5，值为其平方
squared_dict = {x: x**2 for x in range(1, 6)}

print(squared_dict)

# 创建一个嵌套字典
nested_dict = {
    'first_person': {'name': 'Alice', 'age': 25},
    'second_person': {'name': 'Bob', 'age': 30}
}

print(nested_dict)

# 列表推导式：创建一个包含0到9每个数字平方的列表
squared_list = [x**2 for x in range(10)]

print(squared_list)

# 集合推导式：创建一个包含0到9内所有偶数的集合
even_set = {x for x in range(10) if x % 2 == 0}

print(even_set)

# 字典推导式：创建一个字典，将数字映射到其字符串形式
str_dict = {x: str(x) for x in range(1, 6)}

print(str_dict)
