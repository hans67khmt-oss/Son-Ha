a=input("nhap canh a: ")
b=input("nhap canh b: ")
c=input("nhap canh c: ")
def GTLN(a,b,c):
    max=a
    if b>a:
        max=b
        if c>b:
            max=c
    return max
lonnhat= GTLN(a,b,c)
def GTNN(a,b,c):
    min=a
    if a>b:
        min=b
        if b>c:
            min=c
    return min
nhonhat= GTNN(a,b,c)
print("Gia tri lon nhat la: ",lonnhat)
print("Gia tri nho nhat la: ",nhonhat)

