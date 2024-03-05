# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.


my_list = {
    1: "AaEeIiOoUuLlNnSsTtRrАаВвЕеИиНнОоРрСсТт", 
    2: "DdGgДдКкЛлМмПпУу", 
    3: "BbCcMmPpБбГгЁёЬьЯя", 
    4: "FfHhVvWwYyЙйЫы", 
    5: "KkЖжЗзХхЦцЧч", 
    8: "JjXxШшЭэЮю", 
    10: "QqZzФфЩщЪъ"
}

sqrabble = input('Введите слово: ')
# score = [key for letter in sqrabble for key, value in my_list.items() if letter in value]
# print(sum(score))

score = []

for letter in sqrabble:
    for key, value in my_list.items():
        if letter in value:
            score.append(key)
print(sum(score))
            