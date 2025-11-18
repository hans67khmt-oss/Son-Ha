a=float(input("nhập giá trị a: "))
b=float(input("nhập giá trị b: "))
if a== 0:
    if b== 0:
        print("phương trình vô số nghiệm")
    if b!= 0:
        print("phương trình vô nghiệm")
else:
    nghiệm= -b/a
    print("nghiệm của phương trình là",nghiệm)