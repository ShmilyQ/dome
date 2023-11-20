# 练习：使用字典推导式创建一个字典，键为1到10的整数，值为其平方。

squared_list = {
    x:x**2 for x in range(1,11)
}

print(squared_list)

# 练习：使用集合推导式创建一个集合，包含0到10范围内的所有偶数。

even_set = {x for x in range(1,11) if x % 2 == 0}

print(even_set)