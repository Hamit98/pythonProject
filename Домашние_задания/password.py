if __name__ == '__main__':
    # n = int(input('Введите число:'))
    # for i in range(1, 11):
    #     print(n, "*", i, "=", n*i)
    #s = "Hello World Fucking Man"
    #result = ""
    #for i in s:
    #    if i != ' ':
    #        result = result + i
    # print(result)



    n = int(input())

    factorial = 1

    for i in range(2, n + 1):
        factorial *= i

    print(factorial)

