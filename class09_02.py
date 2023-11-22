# datetime模块用于处理时间日期
# 导入datetime模块
from datetime import datetime

# 获取当前时间
now = datetime.now()

# 时间格式化
date = now.strftime('%Y-%m-%d')
print(date)

# 创建特定日期
some_day = datetime(2020, 1, 1)
print('特定日期：', some_day)

# 计算时间差
time_diff = now - some_day
print('计算时间差：', time_diff)

# collections 模块提供了额外的数据结构。
from collections import Counter, defaultdict, namedtuple

# Counter用于计数字典的子类
cnt = Counter(['app', 'test', 'huawei', 'alibaba', 5])
print('计数：', cnt)

# defaultdict用于提供默认值的字典
d = defaultdict(int)
d['key']
print('默认值字典：', d)

# namedtuple 创建命名元组
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('命名元组：', p.x, p.y)

# json 模块用于解析和生成JSON数据。
import json

# 将Python对象转换为json字符串
data = {"name": "Jack", "age": 19}
json_str = json.dumps(data)
print("JSON字符串：", json_str)
print("Python数据：", data)

# 将JSON字符串解析回Python对象
data_parsed = json.loads(json_str)
print("解析后的数据：", data_parsed)

# os 模块提供了与操作系统交互的功能。
import os

# 获取当前工作目录
cwd = os.getcwd()
print("当前工作目录：", cwd)

# 列出目录内容
print("目录内容：", os.listdir('.'))

# 遍历目录内容
for items in os.listdir():
    print("文件名称：", items)

# random 模块用于生成随机数。
import random

ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
num = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
if num > ran:
    print(f"玩家获胜，玩家点数：{num}，电脑点数：{ran}")
elif num < ran:
    print(f"电脑获胜，玩家点数：{num}，电脑点数：{ran}")
else:
    print(f"平局，玩家点数：{num}，电脑点数：{ran}")
