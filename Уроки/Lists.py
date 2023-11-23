if __name__ == '__main__':
    a = [1, 5, 10, 15, 20]
    result = 0
    for i in range(len(a)):
        result = result + a[i]
        print(f"index: {i},value {a[i]}")
    print(f"result: {result}")
