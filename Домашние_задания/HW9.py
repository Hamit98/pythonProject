if __name__ == '__main__':
    text = "В некотором царстве, в некотором государстве жили-были Дед да Баба. С утра до ночи ели они кашу с молоком."

    words = text.split()

    unique_words = set(words)

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_unique_words = sorted(unique_words)

    for word in sorted_unique_words:
        print(f"'{word}': {word_count[word]}")