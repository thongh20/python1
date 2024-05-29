import time
t=time.localtime()
print(t)
t=time.strftime("%m /%d/%y,%H:%M:%S",t)
print(t)
print(type(t))