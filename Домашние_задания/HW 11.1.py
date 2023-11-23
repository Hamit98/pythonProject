words = ["европа", "анаконда", "ель", "трассировка", "якудза", "единство"]

sorted_words = sorted(map(lambda word: word.upper(), filter(lambda word: 'е' in word, words)))

print(sorted_words)
