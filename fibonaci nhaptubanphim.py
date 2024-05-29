def fibonat(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonat(n-1)+fibonat(n-2)

print(fibonat(12))
n=int(input("mời bạn nhập số fibonat tiếp theo :"))
for i in range(1,n+1,1):
    print(fibonat(i),end=" ")