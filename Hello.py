# 测试连接Git
print("hello world")

ptr = '''这是一段多行字符串。这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''

print(ptr)

age = 20
name = 'Swaroop'
print('My name is {0}, How old is {1}'.format(name, age))

# 保留后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 由于我们正在讨论格式问题，就要注意  print  总是会以一个不可见的“新一行”字符（ \n  ）
# 结尾，因此重复调用  print  将会在相互独立的一行中分别打印。为防止打印过程中出现这一
# 换行符，你可以通过  end  指定其应以空白结尾
print('a', end='')
print('b', end='')
print('c', )
# 指定空格位结尾
print('a', end=' ')
print('b', end=' ')
print('c')
# 转义序列
print('What\'s your name?')
print("What's your name?")
print('This is the first line\nThis is the second line')
print("This is the first sentence. \
This is the second sentence.")

print(r"Newlines are indicated by \n")