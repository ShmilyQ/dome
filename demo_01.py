print("Hello World")

# 在Python中，变量是一个用于存储值的占位符。我们可以根据需要随时改变变量的值。例如，假设我们有一个变量x，我们可以将它的值设置为10：

x = 10

# 接下来，我们可以改变变量x的值：

x = 20

# 在Python中，有多种不同的数据类型，包括整型、浮点型、字符串、列表、元组、字典和布尔型等。每种数据类型都有其特定的用途，我们将在后面的学习过程中详细介绍。
# 下面是一些常见数据类型的示例：

# 整型
num1 = 10
num2 = -10

# 浮点型
float1 = 3.14
float2 = -9.87

# 字符串
str1 = "Hello, world!"
str2 = 'This is a string.'

# 列表
list1 = [1, 2, 3, 4]
list2 = ["apple", "banana", "cherry"]

# 元组
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")

# 字典
dict1 = {"name": "John", "age": 30}
dict2 = {1: "one", 2: "two", 3: "three"}

# 布尔型
bool1 = True
bool2 = False

# 我们可以通过使用type()函数来查看变量的数据类型：

print(type(num1)) # 输出：<class 'int'>
print(type(float1)) # 输出：<class 'float'>
print(type(str1)) # 输出：<class 'str'>
print(type(list1)) # 输出：<class 'list'>
print(type(tuple1)) # 输出：<class 'tuple'>
print(type(dict1)) # 输出：<class 'dict'>
print(type(bool1)) # 输出：<class 'bool'>



# 第一课课后练习

my_name  = "John"
my_age   = 36
favourite_food = "Pizza"
my_list = ["apple", "banana", "cherry"]
my_tuple = ("apple", "banana", "cherry")
my_dict = {"name": "John", "age": 36, "food": "Pizza"}
is_student = False

print(f"名称：{my_name},年龄：{my_age},最喜欢的水果：{favourite_food},五个最喜欢的食物：{my_list},家庭成员：{my_tuple},个人信息：{my_dict},是否是学生：{is_student}")