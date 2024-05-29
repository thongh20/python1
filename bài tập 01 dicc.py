dic={"user1":"123456",
"user2":"123455",
"user3":"123455",
"user4":"123455",
"user5":"123455",
"user6":"123455",
"user7":"123455",
"user8":"123455",
"user9":"123455",
"user10":"123455",
"user11":"123455",
"user12":"123455"

}
user=input("mời bạn nhập user name vào :")
pasword=int(input("mời bạn nhập vào pass :"))
if user not in dic:
    print("user không tồn tại")
else:
    if dic[user]!=pasword:
        print("pasword sai")
    else:
        print("đăng nhập thành công")



##if user in dic:
  ##  if dic[user] == pasword:
    #    print("Đăng nhập thành công!")
        # Thực hiện các hành động sau khi đăng nhập thành công
        # Ví dụ: Hiển thị trang chủ, cho phép truy cập vào các tính năng, v.v.
   # else:
     #   print("Mật khẩu sai!")
#else:
    #print