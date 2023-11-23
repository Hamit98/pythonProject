if __name__ == '__main__':

    s = "аргентина манит негра"
    s = s.replace(" ", "").lower()
    s_reversed = s[::-1]

    if s == s_reversed:
        print("Это палиндром")
    else:
        print("Это не палиндром")