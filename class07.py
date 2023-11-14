# 挑战任务：尝试创建一个字典来存储关于一个人的信息（例如名字、年龄和爱好）。然后，编写一个函数，它接受这个字典作为参数，并返回一个包含个人信息的格式化字符串。最后，尝试使用 try-except 块来处理可能出现的错误。


info = {'name': 'Jack', 'age': 18, 'like': 'PlayGame'}

def myInfo(name, age, like):
    return f'姓名：{name}, 年龄：{age}, 爱好：{like}'

try:
    name = input('请输入你的姓名：')
    age = int(input('请输入你的年龄：'))
    like = input('请输入你的爱好：')
    print(myInfo(name, age, like))
except ValueError:
    print('你的输入有误，请重新输入！')



info = {'name': 'Jack', 'age': 18, 'like': 'PlayGame'}

def myInfo(person):
    
    return f'姓名：{person["name"]}, 年龄：{person["age"]}, 爱好：{person["like"]}'

print(myInfo(info))
