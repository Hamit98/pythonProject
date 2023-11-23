#f = lambda a: a*a
#print(f(12))

# f = lambda a, b=14: a if a >= b else b
# print(f"lambda func: {f(12)}")

# numbers = [9, 5, 3, 6, 2]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(f"lambda func: {squared_numbers}")

# numbers = [9, 5, 3, 6, 2]
# filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(filtered_numbers)

# words = ["Hello", "World", "Alex", "almaty", "!sadasd"]

# sorted_words = sorted(words, key=lambda x:len(x))
# print(sorted_words)

# people = [
#     {
#         "name": "Hamit",
#         "age": "24"
#     }, {
#         "name": "Oleg",
#         "age": "23"
#     }, {
#         "name": "Arman",
#         "age": "25"
#     }
# ]
#
# sorted_people = sorted(people, key=lambda x: x["age"])
# print(sorted_people)


# people = [
#     {
#         "name": "Hamit",
#         "age": 70
#     }, {
#         "name": "Oleg",
#         "age": 13
#     }, {
#         "name": "Arman",
#         "age": 56
#     }
# ]
#
# under_30 = list(filter(lambda x: x["age"] >= 30, people))
# beyond_30 = list(filter(lambda x: x["age"] < 30, people))
# print(under_30)
# print(beyond_30)

plus = lambda x, y: a + b
minus = lambda x, y: a - b
delen = lambda x, y: a / b
umnoz = lambda x, y: a * b

a = int(input("a = "))
b = int(input("b = "))
operator = input("op = ")

if operator == "+":
    result = plus(a, b)
elif operator == "-":
    result = minus(a, b)
elif operator == "/":
    result = delen(a, b)
elif operator == "*":
    result = umnoz(a, b)

print(f"result: {result}")

