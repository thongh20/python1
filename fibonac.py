def fibonacia(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacia(n-1)+fibonacia(n-2)
a=fibonacia(12)
print(a)
n=int(input("nhập vào kiểu dữ liệu n vào đây :"))
for i in range(1,n+1,1):
    print(fibonacia(i),end=" ")

