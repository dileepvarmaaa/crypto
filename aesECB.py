from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
x = AES.new(key, AES.MODE_ECB)
ct = x.encrypt('dileepvarmaaaaaa')
print(ct)
pt = x.decrypt(ct)
print(pt)