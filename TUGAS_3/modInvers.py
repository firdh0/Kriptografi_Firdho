def modInvers(a, b):
    for i in range(1, b):
        if(((a % b) * (i % b)) % b == 1):
            return i
    return -1

a = 3
b = 13
print(modInvers(a, b))