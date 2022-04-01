def gcdExtend(a, b):
    if a == 0 :
        return b, 0, 1
     
    gcd, x1, y1 = gcdExtend(b % a, a)

    x = y1 - x1 * (b//a) 
    y = x1

    return gcd, x, y
    del(gcd, x1, y1)
 
a = 26513
b = 32321
g, x, y = gcdExtend(a, b)
print("gcd(", a , "," , b, ") = ", g)
print("crypto{{{},{}}}".format(x,y))

del(a, b, g, x, y)