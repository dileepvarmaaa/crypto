ciphertext = input("ciphertext: ") 
def padding(ciphertext):
	a= len(ciphertext)%16
	if (a<16):
		return (ciphertext+((16-a)*chr(16-a)))
	elif(a==0):
		return (ciphertext+(16*chr(16)))
	else:
		return (ciphertext+((a)*chr(a)))
x=''
x= padding(ciphertext)
print(x)

def checking(ciphertext):
	x = ord(ciphertext[-1])
	if(x==0 or x>16):
		return "wrong padding"
		
	flag = 0
	for i in range (1,x+1):
		if(ciphertext[-i]!=ciphertext[-1]):
			flag=1
	if(flag==0):
		return "correct padding"
	else:
		return "wrong padding"

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
iv = get_random_bytes(16)

def encrypt(pt,key,iv):
	x=AES.new(key,AES.MODE_CBC,iv)
	return iv+x.encrypt(padding(pt))

def decrypt(ct,key,iv):
	y= AES.new(key,AES.MODE_CBC,iv)
	return checking(y.decrypt(ct))

def padding_oracle(ct):
	text=""
	for a in range (2,1,-1):
		plaintext=""
		c1="\x00"*16
		c2=ct[16*(a-1):16*a]  
		c=c1+c2
		for i in range (1,17):
			for j in range (256):
				x=c[:16-i]+chr(j)+c[16-i+1:]  
				if(decrypt(x,key,iv)=="padded already"):
					plaintext=plaintext+chr(i ^ ord(ct[16*(a-1)-i]) ^ j )  
					for x in range (i,0,-1):
						c=c[:16-x]+ chr(i+1 ^ ord(p[x-1]) ^ ord(ct[16*(a-1)-x])) +c2
					break
		text=plaintext[::-1]+text
	return (text)

if __name__=="__main__":
		
		from Crypto.Cipher import AES
		from Crypto.Random import get_random_bytes
		from os import urandom
		
		iv = urandom(16)
		key = urandom(16)
		pt = ""

		ct=encrypt(pt,key,iv)
		print(padding_oracle(pt))

