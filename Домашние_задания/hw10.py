def anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = "пенсионерка"
word2 = "покраснение"

if anagrams(word1, word2):
    print(f"{word1} и {word2} - анаграммы.")
else:
    print(f"{word1} и {word2} - не анаграммы.")




