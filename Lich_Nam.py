a=int(input("nhập tháng: "))
b=int(input("nhập năm: "))
if a<12:
    if a==2:
        for i in range(1,29):
            print(i)
    elif a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        for i in range(1,32):
            print(i)
    else:
        for i in range(1,30):
            print(i)
            