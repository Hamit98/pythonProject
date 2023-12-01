from cryptography.fernet import Fernet
import os

spy_reports_path = 'spy_reports'

decrypted_reports_path = 'decrypted_reports'

encrypted_reports_path = 'encrypted_reports'

key_path = 'spy.key'
with open(key_path, 'rb') as key_file:
    key = key_file.read()

if key:
    cipher = Fernet(key)

    for file_name in os.listdir(decrypted_reports_path):
        file_path = os.path.join(decrypted_reports_path, file_name)

        if 'c' not in file_name.lower():
            with open(file_path, 'rb') as file_to_encrypt:
                data_to_encrypt = file_to_encrypt.read()

            encrypted_data = cipher.encrypt(data_to_encrypt)

            encrypted_file_name = f"{file_name.split('.')[0]}"

            encrypted_file_path = os.path.join(encrypted_reports_path, encrypted_file_name)

            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            print(f"Файл {file_name} успешно зашифрован и сохранен в {encrypted_file_path}")
        else:
            print(f"Пропуск файла {file_name}, так как содержит букву 'c' в названии.")
else:
    print("Ошибка: Ключ для шифрования не найден.")

