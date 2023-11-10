'''
第4课：数据结构
在Python中，数据结构是用来存储、组织和管理数据的方式。Python提供了几种内置的数据结构，这些结构非常强大而且灵活。我们将讨论四种主要的数据结构：列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）。

列表（List）
列表是Python中最基本的数据结构。列表是有序的集合，可以包含任意类型的对象，并且是可变的，即可以改变其内容。

python
Copy code
# 创建列表
fruits = ['apple', 'banana', 'cherry']

# 添加元素
fruits.append('orange')

# 访问列表
print(fruits[0])  # 输出 'apple'

# 列表切片
print(fruits[1:3])  # 输出 ['banana', 'cherry']

# 遍历列表
for fruit in fruits:
    print(fruit)
元组（Tuple）
元组与列表类似，但是元组是不可变的，这意味着一旦创建，你就不能添加、删除或更改元组的元素。

python
Copy code
# 创建元组
coordinates = (10.0, 20.0)

# 访问元组
print(coordinates[0])  # 输出 10.0

# 尝试修改元组（会报错）
# coordinates[0] = 15.0  # TypeError: 'tuple' object does not support item assignment
字典（Dictionary）
字典是一种可变容器模型，可以存储任意类型对象，如字符串、整数、元组等。每个元素都是一个键值对。

python
Copy code
# 创建字典
person = {'name': 'Jack', 'age': 30}

# 访问字典
print(person['name'])  # 输出 'Jack'

# 添加键值对
person['gender'] = 'male'

# 遍历字典
for key, value in person.items():
    print(f"{key}: {value}")
集合（Set）
集合是一个无序的不重复元素集。基本功能包括关系测试和消除重复元素。

python
Copy code
# 创建集合
s = {1, 2, 3, 2, 1}

# 查看集合
print(s)  # 输出 {1, 2, 3}

# 添加元素
s.add(4)

# 检查元素是否在集合中
print(3 in s)  # 输出 True

'''

# 课后练习题
# 创建一个包含不同类型元素的列表，然后添加新元素、修改和删除列表中的元素。

list = [1,'jack',10.2]
print(list)

list.append('one')
print(list)

list[2] = 4
print(list)

list.remove(1)
print(list)
# 创建一个元组，并尝试遍历它的元素。

tup = (10.0, 20.0, 30.0)

for tups in tup :
    print(tups)

# 创建一个字典，包含一些描述您或者某个对象的键值对，并遍历字典的键和值。

dic = {"name":"Jack","age": 18,"sex":"男"}
print(dic)

dic["address"] = "上海"
print(dic)

dic["address"] = "上海-浦东新区"
print(dic)

for key, value in dic.items() :
    print(key, value)

for key in dic.keys() :
    print(key)

for value in dic.values() :
    print(value)

# 创建一个集合，并使用集合的一些基本操作，如添加元素和测试元素是否存在于集合中。

nums = {1,2,3,4,5}

nums.add(11)

if 11 in nums :
    print('在集合中')
else :
    print('不在集合中')

nums.remove(11)

if 11 in nums :
    print('在集合中')
else :
    print('不在集合中')

for num in nums :

    print(num)

'''
Python中的这四种数据结构—列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）—各有其特点和使用场景：

列表（List）
特点：有序、可变、能够包含多种数据类型的元素。
使用场景：当你需要一个可以修改的有序集合时，列表是一个好选择。例如，处理一系列项目、循环处理数据或者在数据集中添加、删除元素时。
Web开发中的使用：处理表单数据、数据库查询结果、进行列表推导以生成HTML模板中的元素等。
元组（Tuple）
特点：有序、不可变、能够包含多种数据类型的元素。
使用场景：当你需要一个不可改变的有序集合时，元组是合适的。它们通常用于保证数据的完整性，因为它们不能被修改。
Web开发中的使用：通常用于函数返回多个值、在某些操作中保持数据不被改变、作为字典的键等。
字典（Dictionary）
特点：键值对集合、无序、可变、键必须是不可变类型。
使用场景：当你需要建立映射关系时，字典是理想的选择。它们能够高效地根据键检索、添加、删除或修改值。
Web开发中的使用：非常常用，比如存储请求的参数、传递数据给模板、处理JSON数据等。
集合（Set）
特点：无序、元素唯一。
使用场景：当你需要存储一个唯一元素集合并快速判断元素是否存在于集合中时，集合是很好的选择。例如，去除重复项、集合运算（如并集、交集）等。
Web开发中的使用：在处理需要元素唯一性的数据时使用较多，但相比其他三种不那么常见。
在Web开发中，字典是最常用的数据结构之一，因为它天生适合表示键值对数据，这在处理HTTP请求和响应时非常常见。JSON，一种数据交换格式，本质上就是一个字典格式，因此在Web API开发中尤其常见。

列表也相当常用，尤其是当你有一系列数据时，比如从数据库检索出的多行数据，或者在模板中需要迭代显示的数据。

元组和集合在Web开发中的使用频率相对较低，但它们在特定情况下仍然很有用。例如，元组可以作为不可变列表的更轻量级的替代品，而集合可以用于需要确保数据唯一性的场景。

总之，选择哪种数据结构取决于你的具体需求，特别是在考虑到数据是否需要保持有序、是否需要保持唯一性以及是否需要经常修改这些数据。在编写Python代码时，通常会根据上下文和性能考虑选择最合适的数据结构。
'''