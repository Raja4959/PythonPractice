import rsa

public_key, private_key = rsa.newkeys(512)
text_msg = "this is unencrypted text"
encrypted_msg = rsa.encrypt(text_msg.encode(), public_key)
decrypted_msg = rsa.decrypt(encrypted_msg, private_key).decode()

print("Original Text : ", text_msg)
# >>> Original Text :  this is unencrypted text
print("Encrypted Text : ", encrypted_msg)
# >>> Encrypted Text :  b'F\x1b\xd0\xc6\xe7\xf1=\xed\xa8\x87\xf7\x10Rpe\x92a\xb2\xc1\xfbw\xcc\xeb\x1e\xd2!\xd5\xaaE\xe3\xc0T\xb94\x10\x9f\x1dt\xab\xed\xb4\xf8\x84\x10\x97\xe9S\xcc\x89\x0b\xa0\x03\xcaE\x1f\xbd\xd40\xd0P\x91\xab6\r'
print("Decrypted Text : ", decrypted_msg)
# >>> Decrypted Text :  this is unencrypted text


p_key, pvt_key = rsa.newkeys(512)
decrypted_msg2 = rsa.decrypt(encrypted_msg, pvt_key).decode()
print("Decrypted Text : ", decrypted_msg2)
# Traceback (most recent call last):
#   File "C:\Users\rajasan\Documents\Python\hashing_encryption\asymmetric_encryption.py", line 17, in <module>
#     decrypted_msg2 = rsa.decrypt(encrypted_msg, pvt_key).decode()
#   File "C:\Users\rajasan\Documents\Python\.venv\lib\site-packages\rsa\pkcs1.py", line 282, in decrypt
#     raise DecryptionError("Decryption failed")
# rsa.pkcs1.DecryptionError: Decryption failed
