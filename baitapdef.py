def n_phai(n):
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
            if j == 0 or j == n - 1 or i + j == n - 1:
                print("*", end="  ")
            else:
                print(" ", end="  ")
        print()

n=int(input("mời bạn nhập vào số nguyên để tìm n"))
if n%2==0:
    n_phai(n)
else:
    n_trai(n)
