# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.



# import random

# s = int(random.randint(1, 1000))
# p = int(random.randint(1, 1000))

# print(s, end=', ')
# print(p)


# import math

s = 12
p = 27

# d = s ** 2 - 4 * p
# if d > 0:
#     x = round((s - math.sqrt(d))//2)
#     y = round((s + math.sqrt(d))//2)
# elif d == 0:
#     x = s // 2
#     y = x
    
# print(x, y)     



solutions = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if s == i + j and p == i * j:
            solutions.append((min(i, j), max(i, j)))
solutions = list(set(solutions))

for solution in solutions:
    print(solution[0], solution[1]) 