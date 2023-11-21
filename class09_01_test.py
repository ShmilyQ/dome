# 尝试创建一个文本文件，写入一些内容，然后再读取它。

with open('class09.txt', 'w') as file:
    file.write('啦啦啦\n')
    file.write('第二行')

with open('class09.txt', 'r') as file:
    con = file.read()

print(con)
# 使用 readline() 和 readlines() 方法来读取文件。

with open('class09.txt', 'r') as file:
    con = file.readline(7)
    con1 = file.readlines()

print(con1)
print(con)

# 使用 with 语句来自动管理文件的打开和关闭。

with open('class09.txt', 'r') as file:
    for line in file:
        print(line, end='')
