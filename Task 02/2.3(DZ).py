# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример:
n = 512

# 1, 2, 4, 8, 16


kvadrat = 0
for i in range(n):
    kvadrat = 2 ** i
    if kvadrat <= n:
        print(kvadrat)
        i += 1
    else:
        break
        
# Идеал:


# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1