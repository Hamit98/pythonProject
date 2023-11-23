import random
import string

def generate_password():

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = '.+!@#$%^&*'

    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + \
               random.choice(digits) + random.choice(digits) + random.choice(special_chars)

    while len(password) < 8:
        category = random.choice([uppercase_letters, lowercase_letters, digits, special_chars])
        password += random.choice(category)

    return password

password = generate_password()
print("Ваш пароль:", password)