#This code is entitled to Harsh Gandhi.

import array	
pt = raw_input("Enter Plaintext: ")
size = 3 #Block size for CFB mode
print ('Block size: ',size)
count=size-len(str(pt))%size
p=""
if count != size:
	for i in range(0,count):
		p+='x'
    
pt = pt+p
IV=["a","b","c"]

temp=["a","b","c"]

print ("Padded Input according to Block Size: ",pt)
key = input("Enter key for Encryption: ")
NumPT=[]
for i in range(0, len(pt)):
    NumPT.append(0)
for j in range(0,len(pt)):
    NumPT[j] = (ord(pt[j])-97)
    
def encryption_shift(l,h):
	xor=""
	global IV
	global pttemp
        global ct
	for i in range (0,len(IV)):
		xor+=chr(((ord(IV[i])-97)-26+key)+97)
	for i in range (l,h):
		pttemp+=chr(((ord(name[i])-97) ^ (ord(xor[i-l])-97))+97)
	IV=""
	ct+=pttemp
	IV+=xor[0:len(xor)-block_size]
	IV+=pttemp
	
def decryption_shift(l,h):
	global IVtemp
	global pt
	global pttemp
	global dxor
	global temp2
	temp2+=ct[l:h]
	for i in range (0,len(IV)):
		dxor+=chr(((ord(IV[i])-97)-26+key)+97)
	for i in range (l,h):
		pt+=chr(((ord(temp2[i-l])-97) ^ (ord(dxor[i-l])-97))+97)
	IVtemp=""
	IVtemp+=dxor[0:len(dxor)-block_size]
	IVtemp+=temp2
		
print ("Encrypted text is : ")	
for i in range(0,len(pt),size):
	encryption_shift(i,i+size)
print ("")

IV=["a","b","c"]		

print ("Decrypted text is : ")	
for i in range(0,len(pt),size):
	decryption_shift(i,i+size)	
print ("")
