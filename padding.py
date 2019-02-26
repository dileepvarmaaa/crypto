text = input("text: ") 
def padding(text):
	x= len(text)%16
	if (x<16):
		return (text+((16-x)*chr(16-x)))
	
	elif(x==0):
		return (text+(16*chr(16)))
	else:
		return (text+((x)*chr(x)))
s=''
s= padding(text)
print(s)

text = input("text: ")
def unpadding(text):
	a = ord(text[len(text)-1])
	if(text[:a:-1].count[(a-1)] == a):
		txt = text[:len(text)-a]
		return txt
	else:
		return("padding is wrong")	