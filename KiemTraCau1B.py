ds=[]
cacdiem=[]
s=0
for i in range(3):
    a=float(input("nhập điểm môn: "))
    ds.append(a)
print(ds)
for diem in ds:
    cacdiem.append(diem)
    s+=a
if diem >= 4 and s >= 15:
    print("học đều các môn")
else:
    print("học không đều các môn")
        

    