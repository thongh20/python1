d={"một":1,"hai":2,"ba":3}
d2={"tùng":1.65,"hải":1.70, "khoa":1.67}
d3={"tùng":1.65,"tùng ":1.50,"khoa":1.67}
d3["tùng"]=1.75# gán giá trị và thay đổi
d3["hoàng"]=1.90# thêm vào giá trị nếu chua tồn tại
del d3["hoàng"]# xóa hoàng ra khỏi danh sách
print(d2)
print(d3)
print(len(d3))
dci3={"khoa công nghệ thông tin ":{'phòng 1':'lập trình ứng dụng','phòng 2':'lập trình đồ họa','phòng3':'lập trình cơ sở dữ liệu'},'khoa công nghệ hàn':{'phòng 01':'hàn nhiet','phòng 02 ':'hàn hơi','phòng 03':'hàn khói'},'khoa cơ khí chế tạo':{'phòng 01':'cắt ','phòng 02':'hàn','phòng03':'ép lực'}}
print(dci3)
print(dci3["khoa công nghệ thông tin "])