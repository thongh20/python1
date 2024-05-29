lst = []

n = int(input("Mời bạn nhập số lượng phần tử: "))
a=[0]*n
dem=0
for i in range(n):
    a = int(input("Nhập vào phần tử thứ {} : ".format(i+1)))
    if a<5:
        dem+=1
        lst.append(i)
print("danh sách trong list số nhỏ hơn 5 là  : ",dem)
print("Danh sách bạn vừa nhập là số nhỏ hơn 5: ", lst)
#print("các vị trí index trong chuoi là ",lst.index())