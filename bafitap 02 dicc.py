import re

dict_01 = {
    "A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
    "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
    "O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
    "V":4,"W":4,"X":8,"Y":4,"Z":10
}

ls1 = "University of Technology and Education"
stt = ""
lstchu = []
lstso = []

for k in ls1.upper():
    if k == " ":
        stt = stt + k
    elif k in dict_01:
        stt = stt + str(dict_01[k])
        lstchu.append(k)
        lstso.append(dict_01[k])

tong = sum(lstso)

print("Số các chữ cái là ", lstchu)
print("Số các chữ số là ", lstso)
print("Tổng các chữ số là", tong)
print(stt)
