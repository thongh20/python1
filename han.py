def PtB1(a,b):
    if a==0 and b==0 :
        return "Phương trình vô số nghiệm"
    elif a==0 and b!=0:
        return "Phương trình vô nghiệm"
    else:
        return "x={}".format(-b/a)
b=PtB1(6,5)
print(b)