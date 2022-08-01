import hashlib

s = "Python Bootcamp"

hashed_string = hashlib.sha256(s.encode('utf-8')).hexdigest()

print(hashed_string)