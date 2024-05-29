def giaithua(n):
    if n==0:
        return 1
    else:
        return n*giaithua(n-1)
a=giaithua(8)
print(a)