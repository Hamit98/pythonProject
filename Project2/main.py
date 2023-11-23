from cryptography.fernet import Fernet


secret_key = Fernet.generate_key()

fernet_key = Fernet(secret_key)

data = b"Hello world!"

encrypted_data = fernet_key.encrypt(data)

print(encrypted_data)

decrypted_data = fernet_key.decrypt(encrypted_data)
print(decrypted_data)












