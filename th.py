
 def UniMaxtrix(n):
    maxtrix =[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i == j :
                row.append(1)
            else:
                row.append(0)
                maxtrix.append(row)
            return maxtrix
            m=int(input("nhập số nguyên m :"))
        print(UniMaxtrix(m))
        