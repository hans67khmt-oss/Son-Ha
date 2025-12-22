n= int(input("nhap so n: "))
def tu(n):
    s=0
    for i in range(1,n+1):
        s= s+ i
    return s
a= tu(n)
def mau(n):
    x=0
    for i in range(1,n+1):
        x=x+ 2*i
    return x
b = mau(n)
c= a/b
print(c)
        
        