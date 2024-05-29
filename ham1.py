def roi(doanhthu,chiphi):
    return (doanhthu-chiphi)/chiphi
def quyetdinhdautu(roi):
    if roi >=0.75:
        print("bạn nên đầu tư vào thi trường đó")
    else:
        print("bạn không nên đầu tư vào thị trường đó")
print("chương trình tính quỹ")
doanhthu=float(input("mời bạn nhập vào doanh thu của mình : "))
chiphi=float(input("mời bạn nhập vào chi phí của mình : "))
b=roi(doanhthu,chiphi)
a=quyetdinhdautu(b)
print(f"tỷ lệ của bạn là {b}%")
