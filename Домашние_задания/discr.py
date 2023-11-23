import math
def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

a, b, c = 3, 2, 5
discriminant = calculate_discriminant(a, b, c)
print(f"Дискриминант: {discriminant}")