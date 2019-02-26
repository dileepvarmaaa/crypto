from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
iv = get_random_bytes(16)
x = AES.new(key, AES.MODE_CBC,iv)
ct = x.encrypt('dileepvarmaaaaaa')
print(ct)
y = AES.new(key, AES.MODE_CBC,iv)
pt = y.decrypt(ct)
print(pt)