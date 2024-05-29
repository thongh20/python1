n=int(input("mời bạn nhập vào N:"))
for i in range(11):
    for j in range(11):
        if (i == 0 and j in (0, 1, 2, 3, 4, 5)) or (i == 1 and j in (0, 1, 2, 3, 4)) or (
                i == 2 and j in (0, 1, 2, 3)) or (i == 3 and j in (0, 1, 2)) or (i == 4 and j in (0, 1)) or (
                i == 5 and j==n-1) or (i == 6 and j in (0, 1)) or (i == 7 and j in (0, 1, 2)) or (
                i == 8 and j in (0, 1, 2, 3)) or (i == 9 and j in (0, 1, 2, 3, 4)) or (
                i == 9 and j in (0, 1, 2, 3, 4, 5)):
            print("* ", end="  ")
        else:
            print("  ", end="")
    print()