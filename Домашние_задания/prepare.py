import os
import time


desktop_path = os.path.expanduser("~/Desktop")


backup_folder = os.path.join(desktop_path, "backups")


current_date = time.strftime("%Y_%m_%d")

start_date = time.mktime(time.strptime("2023-10-01", "%Y-%m-%d"))
end_date = time.mktime(time.strptime("2023-10-31", "%Y-%m-%d"))

while start_date <= end_date:
    backup_date = time.strftime("%Y_%m_%d", time.localtime(start_date))
    backup_file = os.path.join(backup_folder, f"db_backup_{backup_date}.txt")


with open(backup_file, "w") as file:
    file.write("Содержимое файла")

start_date += 24 * 60 * 60  # 1 день в секундах