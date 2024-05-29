d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},

]
for dong in d:
    phone_check=(dong["phone"])
    if (phone_check[-1]) =="8":
        nam_show=dong["name"]
        phone_show=dong["phone"]
        email_show=dong["email"]
        print("name ",nam_show)
        print("*"*40)
        print("phone",phone_show)
        print("email",email_show)