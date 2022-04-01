def power(a, b, p):
    if(b == 0):
        return 1

    temp = power(a, b//2, p) % p
    temp = (temp * temp) % p

    return temp if(b % 2 == 0) else (a * temp) % p
    del(temp)

a = 273246787654
b = 65536
p = 65537
print(power(a, b, p))
del(a, b, p)

# ========== SOLUTION ==========
# from math import gcd

# a = 273246787654
# p = 65537

# if gcd(a,p)==1: #a and p are coprime
#         print(1)

# del(a, p)