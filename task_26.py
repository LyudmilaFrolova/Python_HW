def stepen(a,b):
    a=int(input('a--> '))
    b=int(input('b--> '))
    if a==b==1:
        return 1
    return pow(a,b)
print(stepen(2,3))