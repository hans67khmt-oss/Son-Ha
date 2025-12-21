a= int(input("nhập số a: "))
s=0
for i in range(1, a+1):
    if i%2==0 and i%3==0:
        s += i
        print("tổng là: ",s)
    