import random
import time

year = 2024
print("Chào mừng bạn đến với games tài xỉu của Thông")
mk = "Nguyễn Văn Thông"
lst = ["6B 7C AB FE FF", "7B 7C AB FE FF", "8B 7C AB FE FF", "9B 7C AB FE FF", "5B 7C AB FE FF"]

hovaten = input("Mời bạn nhập Họ và Tên của bạn vào đây :")
ngaythangnamsinh = input("Mời bạn nhập ngày tháng năm sinh của bạn vào đây :")
tuoi = int(input("Mời bạn nhập năm sinh của bạn vào đây :"))
hientai = (year - tuoi)

print(f"Bạn Họ Tên Đầy đủ là {hovaten}, ngày sinh và năm {ngaythangnamsinh}, tuổi hiện tại của bạn là {hientai}")

s = input("Nhập mã thành viên của bạn vào đây :")
d = ""
while True:
    dem = 0
    while s not in lst:
        dem += 1
        if dem == 5:
            print("Bạn đã đăng nhập vào hệ thống quá 5 lần. Hệ thống chuẩn bị thoát.")
            break
        s = input(f"Bạn đã đăng nhập mã thành viên của bạn quá {dem}/5 lần. Mời bạn thử lại: ")
    else:
        print("Đăng nhập thành công")
        log = True

    d = input("Mời bạn đăng nhập mật khẩu để đăng nhập vào Hệ Thống: ")
    dem = 0
    while d != mk:
        dem += 1
        if dem == 3:
            print("Mật khẩu của bạn đã đăng nhập sai quá 3 lần và chuẩn bị khóa.")
            break
        d = input(f"Tài khoản của bạn đã đăng nhập sai quá {dem}/3 lần. Mời bạn thử lại: ")
    else:
        print("Bạn đã đăng nhập thành công. Chuẩn bị bắt đầu trò chơi nào.")
        time.sleep(5)
        print("Bắt Đầu")
        break

# thêm 1 tý gian lận vào đây :))
botdoan=random.randrange(1,6)
if botdoan %2==0:
    print("số chẵn nè",botdoan)
else:
    print("số lẻ nè",botdoan)
bandoan=int(input("mời bạn nhập kết quả Chẵn hay lẻ :"))

dem=0
while bandoan !=botdoan:
    if bandoan>botdoan:
        print("số bạn đoán quá cao")
    elif bandoan <botdoan:
        print("số bạn đoán quá thấp")
        dem+=1
        if dem== 2:
            print("đoán sai 2 lần hệ thông chương trình chuẩn bị thoát nè sau 6 giây nữa")
            time.sleep(6)
            print("Games Over")
            break
    bandoan=int(input(f"mời bạn đoán thên 1 lần nữa {dem+1}/5 lần"))
else:
 print("bạn đã đoán đúmg ")
 time.sleep(2)
 print("bạn có 1 phần thưởng nè")
 time.sleep(2)

 for i in range(7):
     for j in range(7):
         if (i == 0 and j in (1, 2, 3, 4, 5)) or \
                 (i == 1 and j in (0, 3, 6)) or \
                 (i == 2 and j in (0, 6)) or \
                 (i == 3 and j in (1, 5)) or \
                 (i == 4 and j in (2, 4)) or \
                 (i == 5 and j == 3):
             print("*", end=" ")
         else:
             print("  ", end="")
     print()
time.sleep(2)
print("bạn là gay")