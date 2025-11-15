a= float(input("nhập số a: "))
b= float(input("nhập số b: "))
c= float(input("nhập số c: "))
if a == b == c:
  print("tam giác đều")
elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
  print("tam giác vuông")
elif (a==b) or (b==c) or (c==a):
  print("tam giác cân")
else:
  print("tam giác thường")