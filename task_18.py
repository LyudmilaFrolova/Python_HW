lst = list()
n = int(input('введите длину списка: '))  
for i in range(n):
    i = int(input('--> '))
    lst.append(i)
print(lst)  
k = int(input('введите число для проверки: '))
y = abs(k - lst[0])
index = 0
for j in range(1, n):
    count = abs(k - lst[j])
    if count < y:
        y = count
        index = j
print(f'Число {lst[index]} больше всего совпадает с {k}')
