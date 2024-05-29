import time
giay=time.time()
print(giay)

bayh =time.ctime(giay)
print(bayh)

print("mời bạn nhập vào kết quả hạn là 5 giây")

print("bạn đã hết gio")
tg=time.localtime()
print(tg)
print("năm hiện tại là ",tg.tm_year)
print("tháng hiện tại là ",tg.tm_mon)
print("Hôm nay là thu 2 ",tg.tm_wday)
ham=time.strftime("%m/%d/%y,%H:%M:%S",t)
print(ham)
print(type(ham))