#!/usr/bin/env python3
from numpy import busday_offset

data   = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
text   = bytes.fromhex(data)
print(text)

for i in range(256):
    try:
        flag = ''.join(chr(d ^ i) for d in text)
        print(str(i) + ":" + flag)
    except:
        print("error")

