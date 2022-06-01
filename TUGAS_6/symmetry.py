import requests

ciphertext_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt_flag/').json()
print(ciphertext_hex)
ciphertext = ciphertext_hex['ciphertext']
print(ciphertext)

iv = ciphertext[:32]
print(iv)

plaintext = ciphertext[32:]
print(plaintext)

ciphertext_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt/{}/{}'.format(plaintext, iv)).json()
ciphertext = ciphertext_hex['ciphertext']
print(ciphertext)

flag = bytes.fromhex(ciphertext)
print(flag.decode())

# crypto{0fb_15_5ymm37r1c4l_!!!11!}