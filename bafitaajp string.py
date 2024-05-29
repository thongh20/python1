# viết chương trình in ra ký tự để tìm
b="unlversliy of techology and education"

for i in range(len(b)): # duyệt các phần tử trong mảng b cho nó chạy
    if b[i]=="a":
        print("số ký tự index của a là ",i,end=" ")

c="unlversliy of techology and education"
c2=" " # cách 2
for i in range(len(c)):
   if b[i]=="a":
      c2=c2+" " +str(i)
print("sô ky tự index của phần tử a là ",c2 ,end=" ")

# bài tập 2  viết chương trình tạo ra 1  chuỗi nhân đôi ký tự  nhập từ bàn phím ví dụ hello thì in ra hhelllloo)
n=input("mời bạn nhập chuỗi n từ bàn phím để kiểm tra có nhân đôi hay không :")
n1=" "
for i in n :
    if n.islower():
        n1=n*2
    print("trường hop này của bạn nhân đôi được",n1)
# cách 2
n12=input("mời bạn nhập vào ký tự n :")
s=""
for i in n12:
    s=s+i+i
    print(s)
