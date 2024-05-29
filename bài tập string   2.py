
n=input("mời bạn nhập mat khẩu gồm 10 chữ cái cả hoa cả thường : ")
x=bool
y=bool
print(x,y)
while True:
    for i in n:
        if i.isdigit():
            x = True
            break
        else:
            x = False
        for i in n:
            if i.isalpha():
                y = True
            break
        else:
            y=False
    if len(n)<6 or x==False or y==False:
        n=input("mời bạn nhập lại mk chứa ít nhất 6 ký tự cả hoa và thường")
    else:
        print("mật khẩu hợp lệ")
    s=input("mời bạn nhập mk để đăng nhập vào hệ thống")
    dem=0
    while s !=n:
        dem=dem+1
        s=input(f"bạn đã đăng nhập sai bạn còn số lần nhập lại {dem}/5 lần")
        if dem==5:
    print("bạn đã nhập sai quá 5 lần và hệ thống chuẩn bị thoát")

 else:
 print("bạn đã đăng nhap thành công")
    break