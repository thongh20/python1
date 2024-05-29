
n=input("mời bạn nhập danh sách duyệt vào đây :")
s=""
s1=""
for i in n:
   if i.isalpha():
       s+=i
   elif i.isdigit():
       s1+=i
print("dãy chữ là",s)
print("dãy số là ",s1)
