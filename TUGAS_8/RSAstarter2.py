msg = 12
e = 65537
p = 17
q = 23
N = p*q

result = pow(msg, e, N)
print(result)