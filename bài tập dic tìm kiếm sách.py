
mybooks=[
{"Title": "Android App Development", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
{"Title": "Python", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
{"Title": "JavaScript", "Author": "Pham Dieu",
"Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
{"Title": "HTML5", "Author": "Man Nhi",
"Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
{"Title": "Compiler", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
{"Title": "C language", "Author": "Man Nhi",
"Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
{"Title": "Programming Linguistics", "Author": "Pham Dieu",
"Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
{"Title": "C# language", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "42000","Published_Year": "2013"},
{"Title": "App Inventor", "Author": "Man Nhi",
"Publisher": "LD", "Price": "30000","Published_Year": "2015"},
]
check=False
while check==False:
    timkiem=(input("""mời bạn nhập vào kết quả tìm kiếm :
     1.Title
     2.Author
    3.Publicsher
    select(1,2,3):"""))
    if timkiem =="1":
        kwd="Title"
        break
    elif timkiem=="2":
        kwd="Author"
        break
    elif timkiem=="3":
        kwd="Publisher"
        break
    else:
        print("số của bạn không có dữ liệu trong này")
        check=False
dem=0
innput_kskeyword =(input("mười bạn tìm kiếm key word : "))
for dong in mybooks:
    if innput_kskeyword ==(dong[kwd]):
        print("Title= ",dong["Title"])
        print("Author =" ,dong["Author"])
        print("Pulisher = ",dong["Publisher"])
        print("Price = ",dong["Price"])
        print("năm xuất bản =",dong["Published_Year"])
        print("*"*50)
        dem+=1
    elif dem==0:
        print("chương trình của bạn không tồn tại")

