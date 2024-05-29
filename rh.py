while True :
    hoten=input("mời bạn nhập họ tên của bạn vào đây")
    monhoc=input("môn dự thi của bạn là ")
    diem =float(input("nhap diểm của bạn và đây"))
    print(f"Họ tên của bạn là ",[hoten],"môn học của bạn là ",{monhoc},"điểm của bạn là ",{diem})
    if diem >=7:
        print("Bạn đã đủ điều kiện dự thi")
    else:
        print("bạn không đủ điều kien dự thi")
        dung=input("nhập bất kì để tiếp tục " + "hoặc có thể bam  chọn n bỏ qua")
        if dung == "n" or dung=="N":
            break
