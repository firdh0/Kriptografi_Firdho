#!/usr/bin/env python3

# chr => ASCII to Character
# ord => Character to ASCII

coba = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]



# ----- ASCII to character -----
flag = "".join(chr(o) for o in coba)
print(flag)
# print("".join(chr(o) for o in coba))



# ----- character to ASCII -----
asciiValue = []
for character in flag:
   asciiValue.append(ord(character))
# asciiValue = [ord(character) for character in a_string]
print(asciiValue)


