
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise MyCustomException("Это мое пользовательское исключение")

except MyCustomException as e:
    print(f"Поймано пользовательское исключение: {e}")