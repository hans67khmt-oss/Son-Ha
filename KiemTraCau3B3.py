ds=[]
s=0
dss=[]
dsss=[]
m= int(input("m= "))
for i in range(1,m+1):
    a=int(input("nhập danh sách: "))
    ds.append(a)

def is_armstrong(n):
        
            if n<0:
                return False
            str_n= str(n)
            k = len(str_n)
            total=0
            for digit in str_n:
                total += int(digit)**k
            return total == n
           
for n in ds:
    b=is_armstrong(n)
    if b== True:
        d=n
        dsss.append(d)
        s+=1
print(f"so armstrong là: {s}")
print(dsss)


    
