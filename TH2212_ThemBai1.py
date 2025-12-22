a=float(input("nhap canh a: "))
b=float(input("nhap canh b: "))
c=float(input("nhap canh c: "))
while a+b<=c or a+c<=b or c+b<=a:
    print("Nhap lai!")
    a=float(input("nhap canh a: "))
    b=float(input("nhap canh b: "))
    c=float(input("nhap canh c: "))
if a+b>c or a+c>b or c+b>a:
    p= a+b+c
    s=((p/2)*(p/2-a)*(p/2-b)*(p/2-c))**0.5
    print(f"dien tich hinh chu nhat la: {p:.2f}")
    print(f"chu vi hinh chu nhat la: {s:.2f}")

    
    
    
