def n_Phai(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1 or i == j:
                print("*", end="  ")
            else:
                print(" ", end="  ")
        print()

def n_trai(n):
    for i in range(n):
        for j in range(n):
            if j==0 or j== n-1 or i+j==n-1:
                print("* ",end=" ")
            else:
                print(" ", end="  ")
        print()

n=int(input("mời bạn nhập số để tìm n trái và phải "))
if n%2==0:
    n_Phai(n)
else:
    n_trai(n)
