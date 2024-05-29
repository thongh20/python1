a="tôi chăm học tôi chịu khó , tôi đẹp trai,tôi"
for i in a:
    n=a.count("tôi")
print("số từ tôi trong đoạn code này là : ",n)


# cách 2

a1="tôi chăm học tôi chịu khó, tôi đẹp trai , tôi"
dem=0
for i in range(len(a1)):
    if a1[i]=="t" and a1[i+1]=="ô" and a1[i+2]=="i":
        dem=dem+1
print(dem)