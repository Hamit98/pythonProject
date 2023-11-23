try:
    with open('prikol.txt', 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print(f"Произошла ошибка: {e}")



try:
    with open('prikol.txt', 'w') as file:
        file.write("Пример текста для домашнего задания, тут всякая всячина.")
except Exception as e:
    print(f"Произошла ошибка: {e}")