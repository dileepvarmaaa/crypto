from Crypto.Cipher import AES
from Crypto.Util import Counter
from os import urandom

pt    = raw_input()
key   = urandom(16)        
nonce = urandom(12)   

def CTR_encryption(pt,key,nonce):
	ctr = Counter.new(32, prefix=nonce)
	c = AES.new(key, AES.MODE_CTR, counter=ctr) 
	ct = c.encrypt(pt) 
	return ct

def CTR_decryption(ct,key,nonce):
	ctr = Counter.new(32, prefix=nonce)
	c = AES.new(key, AES.MODE_CTR, counter=ctr)
	pt=c.decrypt(ct)  
	return pt

ct=CTR_encryption(pt,key,nonce) 
pt=CTR_decryption(ct,key,nonce)

def main():
	if __name__=="__main__":
		main()
print(ct)
print(pt)

