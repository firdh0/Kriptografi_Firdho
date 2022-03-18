#!/usr/bin/env python3
from pwn import xor

data   = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
uncode = bytes.fromhex(data)
#print(uncode)

first = "crypto{"
key   = xor(uncode[:7], "crypto{").decode() + 'y'
# tanpa decode => b'myXORke'
# dgan  decode => myXORke  

complete_key = (key * (len(data)//len(key)+1))[:len(data)]

flag = xor(uncode, complete_key)
print(flag.decode())
