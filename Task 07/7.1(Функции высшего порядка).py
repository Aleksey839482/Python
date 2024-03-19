# def имя(атрибуты):
#     тело функции
#     что то возвращает, если не чего не прописано но non
    
    
# lambda x, y: x + y        анонимная однострочная функция если функцию нужно использовать один раз и больше нет

# def func(a, b):
#     result = []
#     for i in range(a, b):
#         if i > 0:
#             result.append(i)
#         # elif i < 0:                   #Если есть elif то запись фиговая лямбды
#         #     result.append(i * -1)
#         else:
#             result.append(None)
#     return result

# lambda x, y: [i if i > 0 else None for i in range(x, y)]

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Пример c функцией высшего порядка map и lambda:


# my_list = list('1234567890')
# print(my_list)                              #Сумму элементов не селать со строками

# # for i in range(len(my_list)):
# #     my_list[i] = int(my_list[i])          #Вместо этой записи можно использовать функцию map

# # def add_a(x):
# #     return x + 'A'                        #Вместо этого можно использовать функцию lambda

# # my_list = list(map(lambda x: x * 3, my_list))           #Если используем много раз

# # my_list = list(map(int, my_list))
# # print(my_list)

# # # def odd_filter(x):
# # #     return x % 2 == 0

# # my_list = list(filter(lambda x: x % 2 == 0, my_list))
# # print(my_list)

# # print(sum(my_list))

# my_list = [int(i) for i in my_list if int(i) % 2 == 0]          #Лист компрехеншн
# print(my_list)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. 
# Гарантируется, что самая далекая планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10
from math import pi

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(a, b):
#     if a != b:
#         return pi * a * b
    
# my_list = []
# for i in orbits:
#     if i[0] != i[1]:
#         my_list.append((find_farthest_orbit(*i), *i))
# max_planet = max(my_list)
# print(*max_planet[1:])

def find_farthest_orbit(list_of_orbits):
    orbits_list = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    # print(orbits_list)
    orbits_list = list(map(lambda x: (x, x[0] * x[1]), orbits_list))
    # print(orbits_list)
    return max(orbits_list, key=lambda x: x[1])[0]

print(* find_farthest_orbit(orbits))


