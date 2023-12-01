from cryptography.fernet import Fernet
import os

encrypted_reports_path = 'spy_reports'

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

            decrypted_text = decrypted_data.decode('utf-8')

            modified_text = decrypted_text.replace('вра', 'дру', -1)

            modified_text += "\nПроверено!"

            print(modified_text)

        else:
            print(f"Отчет {file_name} отсутствует.")
else:
    print("Ошибка: Ключ для дешифрования не найден.")