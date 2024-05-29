lst=["6B 7C AB FE FF","7B 7C AB FE FF","8B 7C AB FE FF","9B 7C AB FE FF","5B 7C AB FE FF"]
mk="Nguyen van Thong"
s=input("Mời bạn nhập vào đây để quét mã : ")
import time
d=""
while   True:
    dem =0
    while (s in lst )== False:
        dem = dem+1
        s=input(f"Mời bạn quét lại thẻ của bạn bị sai {dem}/5 lần")
        if dem ==4:
            print("bạn đã quét sai quá 5 lần"+"hệ thống chuẩn bị thoát")
            break
    else:
        print("Đăng nhập thành công ")
        log = True
        d=input("mời bạn đăng nhập mật khẩu để đăng nhập hệ thống :")
        dem = 0
        while d!=mk:
            dem =dem+1
            d=input(f"bạn nhập mk quá 3 lần  sai {dem}/3 lan) : ")
            if dem ==2:
                print("bạn đã nhập mk quá 3 lầ tài khoản của bạn chuẩn bị khóa ")
                break
        else:
            print("Tài khoản cửa bạn đã mở khóa thành công , của của bạn sẽ khóa trong vòng 2 s ")
            time.sleep(2)
            print("Cửa đã khóa")