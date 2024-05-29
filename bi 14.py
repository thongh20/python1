a=int(input("nhập số nguyên chẵn :"))
n=int(input("nhập số tự nhiên n chẵn "))
if a%2==0:
    for i in range(1,n+1):
        print(i)
        a=a+i
    print("ket quả của ban in ra so chan là ",a)
else:
    print("tôi không thể tính được số le đuoc")
