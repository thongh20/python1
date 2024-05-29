from random import  randrange
n=int(input("mời bạn nhap 1 số ngẫu nhiên bất kì : "))
ls=[0]*n
for i in range(n):
    ls[i]=randrange(10,101)
    print(ls)