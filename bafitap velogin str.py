import time
mk="Nguyễn Văn Thông"
s=input("mời bạn nhập tên đăng nhập của bạn vào yêu cầu cả chữ cái và số : ")
x=bool
y=bool
d=""
for i in s:
   if i.isdigit():
        x=True
   else:
        x=False
for i in s:
     if i.isalpha():
         y=True
     else:
         y=False
print(x,y)
while True:
    dem=0
    while s in mk:
        dem=dem+1
    print(f"bạn đã nhập sai trên {dem}/5")
    if dem ==5:
        print("bạn đã đăng nhập sai quá 5 lần hệ thống chuẩn bị thoát nè")
        break
    else:
            print("đăng nhập thành công")
        log=True
    s=input("mời bạn đăng nhap mật khẩu vào hệ thống để đăng nhập")
    while d!=mk:
            dem =0
     dem=dem+1
   print(f"bạn đã đămg mhaap mk sai ")
