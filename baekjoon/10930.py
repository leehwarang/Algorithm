import hashlib
n = input()
hashobj = hashlib.sha256(n.encode())
hex_dig = hashobj.hexdigest()
print(hex_dig)
