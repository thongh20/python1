n=int(input("mời bạn nhập vào số phần tử: "))
lst=[]
dem=0
while dem <n:
    dem+=1
    print(dem)
    a=int(input("mời bạn nhập số phần tử vào đây: "))
    lst.append(a)

print("số phần tử  trong danh sách bạn bình phương là :",lst)
ls1=[]
for i in lst:
    ls1.append(i**2)
    print(ls1)

    dem1=0
    for i in ls1:

        if i>50:

            dem1+=1
    print(f"những số nhỏ hơn 50 là {dem1} số bạn là : ")


