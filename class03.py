'''
1. if 语句
在Python中，if语句用于基于一定条件执行代码。这个条件可以是任何表达式，其结果可以是True或False。根据这个条件的真值，if语句决定是否执行其内部的代码块。

python
Copy code
# 示例：判断一个数是否为正数
number = int(input("请输入一个数字: "))
if number > 0:
    print("这是一个正数。")
elif number == 0:
    print("这是零。")
else:
    print("这是一个负数。")
在这个例子中，程序首先提示用户输入一个数字，并使用int()函数将输入转换为一个整数（因为input()函数返回的是字符串）。然后，程序使用if语句来判断这个数字是正数、零还是负数，并打印出相应的信息。

2. for 循环
for循环在Python中用于遍历序列类型的数据结构，如列表、元组、字典、集合，以及字符串和range对象。

python
Copy code
# 示例：使用for循环打印1到10的数字
for i in range(1, 11):  # 注意，range的结束值是不包括在内的
    print(i)
range(start, stop, step)函数生成一个序列，从start开始到stop结束，步长为step。如果省略start，则默认从0开始。如果省略step，则默认步长为1。

3. while 循环
while循环会在条件为真的情况下重复执行代码块。如果条件从未为真，则代码块不会执行。

python
Copy code
# 示例：使用while循环询问用户是否要继续
continue_prompt = True

while continue_prompt:
    response = input("是否要继续？(y/n): ")
    if response == 'n':
        continue_prompt = False
在这个例子中，程序会一直循环，直到用户输入'n'。每次循环时，程序都会提示用户是否要继续，并根据用户的输入更新continue_prompt变量的值。
'''

# 课后练习题
# 创建一个程序，使用input()函数获取用户输入的一个数字，然后使用if-elif-else结构来判断这个数字是正数、负数还是零，并打印出相应的信息。

num = int(input('请输入一个整数：'))

if num > 0 :
    print('正数')
elif num < 0 :
    print('负数')
else :
    print('零')

# 写一个for循环，使用range()函数来打印1到10的数字。

for n in range(1, 11) :
    print(n)

# 使用while循环，创建一个简单的交互式程序，询问用户是否要继续执行某个操作，如果用户输入'n'，则退出循环；否则，继续询问。

b = True

while b:
    res = input('是否继续？（y/n）：')
    if res == 'n' :
        b = False
    elif res == 'y' :
        b = True
    else :
        print('请输入正确的指令：“y 继续，n 退出”')