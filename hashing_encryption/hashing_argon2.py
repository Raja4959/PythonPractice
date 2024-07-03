# there is no salt generator in argon2
# if we want we can give a salt string and encode it into bytes
# the legacy methods hash_password, hash_password_raw, verify_password are deprecated
# instead of legacy menthods use PasswordHasher class methods hash and verify


import argon2

# pw = b"rajathegreat"
# hashed_pw1 = argon2.hash_password(pw)  # deprecated
# print("hashed_pw using legacy hash_password : ", hashed_pw1)
# raw_pw = "rajathegreat"
# raw_pw_bytes = raw_pw.encode()
# hashed_raw_pw = argon2.hash_password_raw(raw_pw_bytes)
# print("hashed_pw using legacy hash_password_raw : ", hashed_raw_pw)
# print("verify password for hash_password : ",
#       argon2.verify_password(hashed_pw1, pw))
# print("verify password for hash_password_raw : ",
#       argon2.verify_password(hashed_raw_pw, raw_pw_bytes, type=argon2.Type.ID))
# verify_password is not working for hash_password_raw

str_pw = "rajathegreat"
bytes_pw = str_pw.encode()
hasher = argon2.PasswordHasher()
str_hashed = hasher.hash(str_pw)
bytes_hashed = hasher.hash(bytes_pw)
print("string hashed : ", str_hashed)
print("bytes hashed : ", bytes_hashed)

print("verify string hashed with string pw : ",
      hasher.verify(str_hashed, str_pw))
print("verify string hashed with bytes pw : ",
      hasher.verify(str_hashed, bytes_pw))

print("verify bytes hashed with string pw : ",
      hasher.verify(bytes_hashed, str_pw))
print("verify bytes hashed with bytes pw : ",
      hasher.verify(bytes_hashed, bytes_pw))

print("verify bytes hashed with string pw : ",
      hasher.verify(bytes_hashed, "str_pw"))
print("verify bytes hashed with bytes pw : ",
      hasher.verify(bytes_hashed, b"bytes_pw"))
