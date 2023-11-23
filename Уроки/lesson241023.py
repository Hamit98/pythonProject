if __name__ == '__main__':
    # def volume (a, b, h):
    #     v = a * b * h
    #     return v
    #
    #
    # res = volume(5, 4, 7)
    # print(f"Volume is: {res}")

    # def sum_of_evens (*args):
    #     res = 0
    #     for number in args:
    #         if number % 2 == 0:
    #             res = res + number
    #     return res
    # result = sum_of_evens(2, 5, 10)
    # print(result)

    def mean_value(*args):
        res = 0
        if len(args) == 0:
            return res
        for number in args:
            res = res + number
        mean_v = res / len(args)
        return mean_v
result = mean_value(12, 15, 22, 44)
print(result)