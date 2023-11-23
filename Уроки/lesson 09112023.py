import json
# data_to_write = ["Hello World!\n", "Hi, There!\n"]
# file1 = open("example.txt", "a")
# # file1.write("Hello World!")
# file1.writelines(data_to_write)

# file2 = open("example.txt", "r")
# data = file2.read()
# print(data)

# file1 = open("scratch.json", "w")
# d = {"name": "JustCode", "age": 25}
# json.dump(d, file1)


# with open("example.txt", "w") as file:
#     file.write("Hello World!")
# file.write("Hello World!")


# PART2
#
# class Shkaf:
#     def __init__(self):
#         self.door = "Closed"
#
#     def get_candies(self):
#         if self.door == "Open":
#             print("Взяли все конфеты!")
#         else:
#             print("Дверь закрыта!")
#
#     def open_door(self):
#         self.door = "Open"
#         print("Открыли дверь!")
#
#     def close_door(self):
#         self.door = "Closed"
#         print("Закрыли дверь!")
#
#     def __enter__(self):
#         print("Вы зашли в контекст менеджер!")
#         self.open_door()
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback   ):
#         self.close_door()
#         print("Мы вышли из контекст менеджера!")
#
#
# with Shkaf() as s:
#     s.get_candies()





