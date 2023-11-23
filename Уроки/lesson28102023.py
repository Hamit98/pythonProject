# from math import pi, pow
#
#
# def get_area(r):
#     s = pi * pow(r, 2)
#     return s
#
# def get_v(r):
#     V = 4 / 3 * pi * pow(r, 3)
#     return V
#
# def rad_of_ang(r3):
#     rad = r3 * 180/pi
#     return rad
# r3 = int(input("Градус угла:"))
# r = 12
# area = get_area(r)
# print(f"Area: f{area}")
# print(f"V: {get_v(r)}")
# print(f"Радиан равен: {rad_of_ang(r3)}")
import random
from random import choice, choices

# # a = random.randint(10,15)
# a = random.randrange(10, 15, 3)
# print(a)


# books = ("Kal", "123", "Pook")
# result = choices(books, k=2)
# print(result)


# a = randint(1, 6)
# print(f"Hamit: {a}")
# b = randint(1, 6)
# print(f"Oleg: {b}")
# if a > b:
#     print("Hamit win!")
# elif a < b:


from random import choice

flavors = ["shit", "apple", "bugs", "cream-soda", "orange", "socks"]
(flavors)
flavors = random.choice(flavors)
print(flavors)


