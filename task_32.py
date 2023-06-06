lst=[1,3,5,8,2]
a=int(input('a--> '))
b=int(input('b--> '))
for i in range(len(lst)):
    if lst[i]>a and lst[i]<b:
        print(f'элемент с этим индексом {i} входит в заданный диапазон')