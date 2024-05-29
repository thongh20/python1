import  random
maydoan =random.randrange(1,10)
doan =int(input("bạn hãy dự doán số của bạn vào đây"))
print(maydoan)
while doan !=maydoan:
    if doan >maydoan:
        print(doan,"Số bạn nhap vào cao quá")
    if doan < maydoan:
        print(doan,"Sô bạn đoán thấp quá so với dự tinh")
    doan =int(input("bạn đoán lại đi gần đúng với kết quả rồi "))
print(doan,"Bạn đã thắng")