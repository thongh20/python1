from random import randrange
aray=[]
row =int(input("mời bạn nhập số dòng số cột :"))
colum=int(input("mời bạn nhập số cột : "))
for i in range(colum):
    a=[]
    for j in range(row):
        a.append(randrange(0,21,1))
        aray.append(a)
        print("{:>15}".format(j),end=" ") # có căn chỉnh dòng
    print()

# cách 2
#for z in range(len(aray)):
 #   for u in range(len(aray[z])):
  #      print(aray[z][u],end=" \t ")
    #print()