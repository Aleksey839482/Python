# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint as rnum

count = int(input('Введите количество оценок: '))

notes = []
for i in range(count):
    notes.append(rnum(1, 5))
print(notes)

# max_numbers = 1                                         # Функция max: max(notes)
# min_numbers = 5                                         # Функция min: min(notes)
# notes_1 = []
# for i in range(len(notes)):
#     if notes[i] > max_numbers:
#         max_numbers = notes[i]
#     elif notes[i] < min_numbers:
#         min_numbers = notes[i]

# print(f'Мин - {min_numbers}, Макс - {max_numbers}')

# notes_1 = []
# for i in range(len(notes)):
#     if notes[i] == max_numbers:
#         notes_1.append(min_numbers)
#     else:
#         notes_1.append(notes[i])

# print(notes_1)


# Если сделать по функциям max, min:
max_notes = max(notes)
min_notes = min(notes)

for i in range(len(notes)):
    if notes[i] == max_notes:
        notes[i] = min_notes

print(notes)