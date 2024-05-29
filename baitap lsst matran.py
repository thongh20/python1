dong =4
cot=3
lst=[[1]*dong]*cot
for i in lst:
    for j in i:
        print("{:>5}".format(j),end=" ")
    print()