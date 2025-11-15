a= int(input("nhập số a"))
b= int(input("nhập số b"))
c= int(input("nhập số c"))

if (a + b > c) and (a + c > b) and (b + c > a):
  print("3 số vừa nhập đủ điều kiện trở thành 1 tam giác")
else:
  print("3 số vừa nhập không tạo thành 1 tam giác")