# -*- coding: UTF-8 -*-
import random
from sys import version_info

# 生成个随机字符，该字符包含0-f即可
key = '0123456789abcdef'

# 将列表中的元素打乱顺序
key_list = list(key)
random.shuffle(key_list)
new_key = ''.join(key_list)

# 读取bin内容，并且做hex编码
with open('shellcode.bin', mode='rb') as f:
    if version_info >= (3,0):
        shellcode = f.read().hex()
        print(shellcode)
    else:
        shellcode = f.read().encode('hex')

shellcode_list = []
for i in shellcode:
    # 返回索引值
    value = new_key.find(i)
    shellcode_list.append(value)

print("key: " + new_key)
print("shellcode: " + str(shellcode_list))