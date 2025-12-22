a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))
max= a
min= b
if b>a:
    max=b
    if c>b:
        max=c
else:
    max=a
if a>b:
    min=b
    if b>c:
        min=c
else:
    min=a
print("max",max)
print("min",min)
    
