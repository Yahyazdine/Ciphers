import pyDes

data = raw_input("Enter the data to be encrypted: ")
key = raw_input("Enter the key (length should be 8): ")
while len(key)==8:
    key = raw_input("Enter the key (length should be 8): ")
    
k = pyDes.des(key, pyDes.CBC, "AAAAAAAA", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
print "Encrypted: %r" % d
print "Decrypted: %r" % k.decrypt(d)
assert k.decrypt(d) == data
