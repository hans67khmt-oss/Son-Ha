ds=[]
dss=[]
dsss=[]
n=int(input("n= "))
for i in range(1, n+1):
    a=int(input("nhâp danh sách: "))
    ds.append(a)
for so in ds:
    dss.append(so)
if so%2==0 and so%3==0:
    dsss.append(so)
s=sum(dsss)
print(s)
    

    