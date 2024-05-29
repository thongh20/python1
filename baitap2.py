import time
ten=input("ten cua ban la ")
n=int(input("mời bạn nhập tuoi hiện tại"))
hientai=time.localtime()
nam=hientai.tm_year
print(nam)
print(f" nam,{ten},dat 100 tuoi la",(100-n)+nam)