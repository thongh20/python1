n=int(input("nhập số nguyên để tạo chữ M : "))
for i in range(n):
    for j in range(n):
        if j ==0 or j==n-1 or i==j:
            print("*",end="  ")
        else:
            print(" ", end="  ")
    print()

n=int(input("nhập số nguyên để tạo M Ngược :"))
for i in range(n):
    for j in range(n):
        if j == 0 or j==n-1 or i+j==n-1:
            print("* ", end= " ")
        else:
            print("", end= "")
        print()
        