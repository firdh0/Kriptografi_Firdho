def modInverse(a, m):
	m0 = m
	y = 0
	x = 1

	if (m == 1):
		return 0

	while (a > 1):

		q = a // m

		t = m

		m = a % m
		a = t
		t = y

		y = x - q * y
		x = t

	if (x < 0):
		x = x + m0

	return x

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
N = p*q
t = (p-1)*(q-1)
d = modInverse(e, t)

print(d)
