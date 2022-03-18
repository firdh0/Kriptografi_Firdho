#!/usr/bin/env python3

data = "label"
ascii_ = []
flag = ''

for c in data:
    ascii_ = ord(c) ^ 13
    flag  += chr(ascii_)

# f-string => agar value dapat terbaca di dalam string
print(f'crypto{{{flag}}}')