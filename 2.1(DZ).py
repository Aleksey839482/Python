# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

coins = [0, 0, 0, 0, 1, 1]
# coins = 3

# import random
# RESHKA = 0
# REBRO = 1
# count = 0
# coins = int(input('Введитеколичество монет: '))
# for i in range(coins):
#     coins = random.randint(RESHKA, REBRO)
#     print(coins, end=' ')
#     if coins == REBRO:
#         count += 1
# else:
#     print(f'\n{count}')
RESHKA = 1
GERB = 0
count_r = 0
count_g = 0

for i in coins:
    if i == GERB:
        count_g += 1
    else:
        count_r += 1
if count_r > count_g or count_r == count_g:
    print(count_g)
else:
    print(count_r)


# Типо идеал:

# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)