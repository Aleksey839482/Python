# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# n = int(input('Введите число: '))
# def number(n):
#     d = 2
#     while n % d !=0:                                # Лобовое решение
#         d += 1
#     return d == n
# print(number(n))
    


def is_simple(num):
    if num in (1, 2):
        return True
    if not num % 2: #== 0:
        return False                                    # Быстродействие в 8 раз
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
print(is_simple(10))