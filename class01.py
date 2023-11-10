import datetime

# 获取当前日期
now = datetime.datetime.now()

#格式化日期
date_str = now.strftime("%Y-%m-%d")

print(f"我的名字：Jack，当前日期：{date_str}")