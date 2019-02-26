from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
iv = get_random_bytes(16)
x = AES.new(key, AES.MODE_CBC,iv)
ct = x.encrypt('dileepvarmaaaaaadileepvarmaaaaaa')
if ct[0:16]==ct[16:32]:
	print("ecb mode")
else:
	print("cbc mode")

print(ct)

x = AES.new(key, AES.MODE_ECB)
ct = x.encrypt('dileepvarmaaaaaadileepvarmaaaaaa')
if ct[0:16]==ct[16:32]:
	print("ecb mode")
else:
	print("cbc mode")

print(ct)

