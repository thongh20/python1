import random
import time

maydoan = random.randrange(1, 10)
bandoan = int(input("Mời bạn nhập số ngẫu nhiên để tham gia trò chơi đoán số: "))
dem = 0

while bandoan != maydoan:
    if bandoan > maydoan:
        print(f"{bandoan} Số bạn đưa ra quá cao so với kết quả dự đoán.")
    elif bandoan < maydoan:
        print(f"{bandoan} Số bạn đưa ra quá thấp so với kết quả dự đoán.")
    dem += 1
    if dem == 5:
        print("Bạn đã nhập sai 5 lần và chương trình sẽ đóng sau 6 giây.")
        time.sleep(6)
        print("Chương trình đã thoát")
        break
    bandoan = int(input(f"Mời bạn đoán lại ({dem + 1}/5 lần): "))
else:
    print("Xin chúc mừng! Bạn đã đoán đúng.")