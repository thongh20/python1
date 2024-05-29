lst=[1,2,3,4,5,56,"python"]
lst1=[1,31,4,4]
chieuchai=len(lst)
lst.append(12)# thêm 1 phần tử vào cuối phần tử có thể chứa lst



print("số phần tử nằm ở trong lst là",chieuchai)

print(lst)


dem=lst.count(56) # đêm các phần tử
print(dem)


dac=lst.reverse()#đảo lst
print(dac)
lst.insert(2,900)
print(lst)

a=lst.index("python") # tìm vị trí phần tử của index
ax=lst.extend(lst1)# nối giữa 2 list danh sách
print(ax)
print(a)
ax1=lst.clear()# xóa toàn bộ phần tử trong danh sách lst
print(ax1)
ma=lst1.sordted()# sẽ khôn thay dổi giá trị ban đầu
lst.sort()# sắp xếp theo ký tu tăng dần sẽ thay đổi giá trị ban đầ
print(lst)