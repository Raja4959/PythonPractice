# salt will be encryption key for bcrypt - no need to save the salt values
# when we use checkpw() it automatically compares the passwords and gies accurate results


import bcrypt

password = "rajathegreat"  # str format
binary_pw = password.encode()  # binary format
# bin_pw = b'rajathegreat'  # above two statements generate this result

# generate once and add it to env vars if we want
# The salt value will be diffrent each time and that makes no difference in comparing the passwords
salt = bcrypt.gensalt()  # generates a secret key
print("Salt :", salt)

hashed_pw = bcrypt.hashpw(password=binary_pw, salt=salt)
print("Hashed Password :", hashed_pw)

salt2 = bcrypt.gensalt()
print("Salt2 :", salt2)

password2 = "rajathegreat"  # str format
binary_pw2 = password2.encode()
hashed_pw2 = bcrypt.hashpw(password=binary_pw2, salt=salt2)
print("Hashed Password2 :", hashed_pw2)

is_valid_password = bcrypt.checkpw(binary_pw2, hashed_password=hashed_pw)
print("is_valid_password1 : ", is_valid_password)

is_valid_password2 = bcrypt.checkpw(binary_pw, hashed_password=hashed_pw2)
print("is_valid_password2 : ", is_valid_password2)
