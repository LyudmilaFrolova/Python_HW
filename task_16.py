# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#    -> 1

lst = []
n = int(input('введите количество элементов списка: '))
for i in range(n):
    m = int(input('число: '))
    lst.append(m)
print(lst)
x = int(input('введите число, которое нужно проверить: '))
lst_1 = set(lst)
k = n-len(lst_1)+1
print(f'число {x} встречается {k} раз')