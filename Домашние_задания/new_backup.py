import os
import time


desktop_path = os.path.expanduser("~/Desktop")


backup_folder = os.path.join(desktop_path, "backups")


current_date = time.strftime("%Y_%m_%d")


backup_file = os.path.join(backup_folder, f"db_backup_{current_date}.txt")

if os.path.exists(backup_file):
    print("Резервное копирование уже сделано.")
else:

    with open(backup_file, "w") as file:
        file.write("Содержимое нового резервного файла")
    print("Создан новый файл резервного копирования.")