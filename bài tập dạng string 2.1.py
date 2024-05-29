while True:
    n = input("Mời bạn nhập mật khẩu gồm từ 6 đến 10 ký tự, bao gồm cả chữ hoa và chữ thường: ")
    if (any(i.isdigit() for i in n) and
        any(i.isalpha() for i in n) and
        any(i.islower() for i in n) and
        any(i.isupper() for i in n) and
        6 <= len(n) <= 10):
        print("Mật khẩu hợp lệ.")
        break
    else:
        print("Mật khẩu không hợp lệ. Vui lòng thử lại.")

s = input("Mời bạn nhập mật khẩu để đăng nhập vào hệ thống: ")
dem = 0
while s != n and dem < 5:
    dem += 1
    s = input(f"Bạn đã đăng nhập sai. Bạn còn {5-dem} lần thử lại: ")

if dem == 5:
    print("Bạn đã nhập sai quá 5 lần và hệ thống chuẩn bị thoát.")
else:
    print("Bạn đã đăng nhập thành công.")
