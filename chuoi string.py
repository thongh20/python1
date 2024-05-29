A="abcxys"
B="1234"
c="     "
D="SẤDADADADA"
F="Acmmfk"
t="gágaaa;gaghhahgbbb"
print(A.isalnum())
print(A.isalpha()) # trả về true khi trữ là chữ cái
print(B.isdigit())# true trả về khi có tring là số
print(c.isspace())# khi kí tự toàn là cách thì là true
print(A.islower())# kiểm tra ký tự viết thường
print(D.isupper())# kiểm tra chữ hoa
print(F.istitle())# kiểm tra chữ cái đầu viết hoa
print(A.upper())# chuyển toàn bộ chữ cái sang viết hoa
print(A.islower())# chuyển toàn bộ chữ hoa thành chữ thường
nt=t.split(";",1)
print(type(nt))
for i in nt:
 a2=",".join(nt) # dùng để noi xâu
 print(a2)