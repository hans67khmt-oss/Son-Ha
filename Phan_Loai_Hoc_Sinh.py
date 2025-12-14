a = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
for i in range(len(a)):
    if a[i] >=8:
        print(f"học sinh giỏi: {a[i]}")
    elif 6.5<= a[i] <=7.9:
        print(f"học sinh khá: {a[i]}")
    else:
        print(f"học sinh trung bình: {a[i]}")
        
