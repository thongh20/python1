a="abcXYZ"
a1=""
for i in a:
    if a.islower():
        i=i.upper()
    else:
        i=i.lower()
    a1=a1+i
print(a1)