# -*- coding: utf-8 -*-
# 输入任意个字符串，将其中的小写字母变为大写，大写字母变为小写，其他字符不用处理；
# 输入描述:
# 任意字符串：abcd12#%XYZ
# 输出描述:
# 输出字符串：ABCD12#%xyz
import sys
s = sys.stdin.readline().strip()
res = []
for i in s:
    if ord(i) >= ord('A') and ord(i) <= ord('Z'):
        res.append(chr(ord(i) + 32))
    elif ord(i) >= ord('a') and ord(i) <= ord('z'):
        res.append(chr(ord(i) - 32))
    else:
        res.append(i)
print(''.join(res))
