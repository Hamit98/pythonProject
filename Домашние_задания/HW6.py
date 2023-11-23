if __name__ == '__main__':

    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    odd_numbers = []

    for n in original_list:
        if n % 2 != 0:
            odd_numbers.append(n)
    print(odd_numbers)