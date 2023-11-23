from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

encrypted_reports_path = 'spy_reports'

decrypted_reports_path = 'decrypted_reports'

key_path = 'spy.key'
with open(key_path, 'rb') as key_file:
    key = key_file.read()

if key:
    cipher = Fernet(key)

    file_names = [
        "01_10_2023_cachalot.txt",
        "03_10_2023_whale.txt",
        "06_10_2023_cheetah.txt",
        "07_10_2023_gorilla.txt",
        "10_10_2023_dolphin.txt",
        "13_10_2023_tiger.txt",
        "18_10_2023_elephant.txt",
        "19_10_2023_giraffe.txt",
        "21_10_2023_penguin.txt",
        "28_10_2023_koala.txt"
    ]

    for file_name in file_names:
        encrypted_file_path = os.path.join(encrypted_reports_path, f"{file_name}")

        if os.path.exists(encrypted_file_path):
            with open(encrypted_file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            decrypted_data = cipher.decrypt(encrypted_data)

            decrypted_file_name = f"{file_name}_decrypted_report.txt"

            decrypted_file_path = os.path.join(decrypted_reports_path, decrypted_file_name)

            with open(decrypted_file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)

            print(f"Отчет {file_name} успешно дешифрован и сохранен в {decrypted_file_path}")
        else:
            print(f"Отчет {file_name} отсутствует.")
else:
    print("Ошибка: Ключ для дешифрования не найден.")