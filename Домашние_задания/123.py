# if __name__ == '__main__':
#
#     print("Bomb has been planted")
#     number = 10
#     while number != 0:
#         print(number)
#         number -= 1
#     print("BOOOOOOOOOOOOOM!")

if __name__ == '__main__':
    # for n in range(10, 22):
    #     print(n)

    # n = "Hello World!"
    # for x in n:
    #     print(x)
    user_input = input("Вы человек? [Да/Нет]")
    attempts = 3
    incorrect = True
    for i in range (attempts):
        if user_input == 'Да' or user_input == 'Нет':
            print("Спасибо за ответ")
            incorrect = False
            break
        print("Не корректный ответ")
        user_input = input("Вы человек? [Да/Нет]")
    if incorrect:
        print("Отдохните")

