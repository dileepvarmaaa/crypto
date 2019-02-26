from os import urandom
key=urandom(16)
def pad(m):
    padbyte = 16 - (len(m) % 16)
    return m + padbyte*chr(padbyte)

def encryption_ECB(pt,key):
	from Crypto.Cipher import AES
	cipher=AES.new(key,AES.MODE_ECB)	
	ct=cipher.encrypt(pad(pt))
	return (ct)

l=len(encryption_ECB("a",key))

for i in range (1,32):
	if(len(encryption_ECB("a"*i,key))>l):
		print(len(encryption_ECB("a"*i,key))-l)
		break
