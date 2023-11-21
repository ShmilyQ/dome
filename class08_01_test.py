# 创建一个类并实例化对象。

class Animal:

    def __init__(self, name, color):
        self.name = name  # 实例属性
        self.color = color

    # 实例方法
    def info(self):
        return f'这只动物叫：{self.name}，它有着一身的{self.color}色。'


# 实例化对象
aa = Animal('花花', '灰白')
print(aa.info())


# 尝试使用继承和多态。
class Cat(Animal):

    def info(self):
        return f'这只小猫叫：{self.name}，它有着一身的{self.color}色毛发。'


class Dog(Animal):
    def info(self):
        return f'这只小狗叫：{self.name}，它有着一身的{self.color}色毛发。'


cc = Cat('小花', '黄白')
dd = Dog('豆豆', '黑')

# 多态：使用通用接口处理不同类的对象
animals = [cc, dd]

for animal in animals:
    print(animal.info())


# 使用魔术方法如 __str__ 和 __init__。

class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'姓名：{self.name}，年龄：{self.age}'


test = Test('小明', 32)
print(test)