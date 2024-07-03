from cryptography.fernet import Fernet

text_msg = "This is unencrypted Text"

# Save this encryption Key
key1 = Fernet.generate_key()
fernet1 = Fernet(key=key1)

encoded_msg = fernet1.encrypt(text_msg.encode())
decrypted_msg = fernet1.decrypt(encoded_msg).decode()

print("Original Text : ", text_msg)
# >>> Original Text :  This is unencrypted Text
print("Encrypted Text : ", encoded_msg)
# >>> Encrypted Text :  b'gAAAAABmgmNa6ZidTJI4MLG_HHLs5ieTN7CkW6caDQVT2f-OAg0WI7D5zFdeFWi-ccaKsZW6drZ4oLfIUwuzZHvKRj3PV7UJD9rkDmKBk_lnbVURHNJbeXE='
print("Decrypted Text : ", decrypted_msg)
# >>> Decrypted Text :  This is unencrypted Text

key2 = Fernet.generate_key()
fernet2 = Fernet(key=key2)

decrypted_msg2 = fernet2.decrypt(encoded_msg).decode()
print("Decrypted Text with different Key : ", decrypted_msg2)
# Traceback (most recent call last):
#   File "C:\Users\rajasan\Documents\Python\.venv\lib\site-packages\cryptography\fernet.py", line 130, in _verify_signature
#     h.verify(data[-32:])
# cryptography.exceptions.InvalidSignature: Signature did not match digest.

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "C:\Users\rajasan\Documents\Python\hashing_encryption\symmetric_encryption.py", line 21, in <module>
#     decrypted_msg2 = fernet2.decrypt(encoded_msg).decode()
#   File "C:\Users\rajasan\Documents\Python\.venv\lib\site-packages\cryptography\fernet.py", line 89, in decrypt
#     return self._decrypt_data(data, timestamp, time_info)
#   File "C:\Users\rajasan\Documents\Python\.venv\lib\site-packages\cryptography\fernet.py", line 148, in _decrypt_data
#     self._verify_signature(data)
#   File "C:\Users\rajasan\Documents\Python\.venv\lib\site-packages\cryptography\fernet.py", line 132, in _verify_signature
#     raise InvalidToken
# cryptography.fernet.InvalidToken
