# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# Пример:
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

def f(a, b):
    if not b:
        return 1
    return f(a, b - 1) * a
        
# a = 3
# b = 5
# print(f(b))

print(f(3, 5))