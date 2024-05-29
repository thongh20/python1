str1 = "tiếng anh = 78, ngữ văn =83, toán =68, lịch sử =65 "
tach = str1.split(',')
s = 0
dem=0
for i in tach:
    num = ''.join(filter(str.isdigit, i))
    if num:
        s = s + int(num)
        dem=dem+1
print(s)
print(f"trung cộng của tất cả các môn là,{s/dem}")