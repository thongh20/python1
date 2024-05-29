from random import randrange
n=int(input("mời bạn nhập n ngẫu  nhiên từ bàn phím : "))

m=int(input("mời bạn nhập ngẫu nhiên n vào bàn phím : "))
for i in range(n):
    lst=[]
    for j in range(m):
        lst.append(randrange(1,100,1))
        print("{:>5}".format(j),end=" ")
        print(lst)
    print("số ma trận lớn nhất trong dãy là : ",max(lst))
