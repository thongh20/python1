matrix=[
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,50018],
    [1,2,3,4,50000]
]
for i in matrix:
    for na in i:
        print("{:<8}".format(na), end=" ")
    print()