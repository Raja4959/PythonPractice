# hashlib don't have the capability of generating salt so it is adviced to store it in env variables
# to match with hashed string we need to follow the process again
# match the hashed strings by getting hexdigest and digest

import hashlib

pw = "rajathegreat"
salt = "n5g"
salted_pw = pw+salt
hashed_pw = hashlib.md5(salted_pw.encode())  # creates hash object
print(type(hashed_pw))
print(hashed_pw.hexdigest())
print(hashed_pw.digest())
