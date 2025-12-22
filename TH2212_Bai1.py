w= float(input("nhap canh w: "))
h= float(input("nhap canh h: "))
while w<0.0 or h>100.0:
    print("nhap lai!")
    w= float(input("nhap canh w: "))
    h= float(input("nhap canh h: "))
if w>=0.0 and h<=100.0:    
  p=(h+w)*2
  s=w*h
  print(f"dien tich hinh chu nhat la: {p:.2f}")
  print(f"chu vi hinh chu nhat la: {s:.2f}")