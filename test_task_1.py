import hashlib

s = "Python Bootcamp"

# using hash() method
hash_value = hash(s)
print(hash_value)

# using module hashlib with SHA256 algorithm
hash_object = hashlib.sha256(s.encode())
print(hash_object.hexdigest())

# using module hashlib with MD5 algorithm
hash_object = hashlib.md5(s.encode())
print(hash_object.hexdigest())
