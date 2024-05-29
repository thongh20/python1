import time
ten =input("nhập tên của bạn là :")
tuoi =int(input("bạn năm nay bao nhiêu tuổi là :"))
hientai =time.localtime()
nam=hientai.tm_year
print(f"nam hien tai là  {nam},dự kiến 100 năm nữa tuoi của bạn là {(100-tuoi)+nam} bạn sẽ 100 tuổi")
