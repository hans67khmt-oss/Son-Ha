a= input("nhập lựa chọn cho người chơi 1: ")
b= input("nhập lựa chọn cho người chơi 2: ")
if ((a == "kéo") or (a == "bao") or (a == "búa")) and ((b == "kéo") or (b == "búa") or (b == "bao")):
    if a == b:
        print("hòa")
    elif ((a == "kéo") and (b == "bao")) or ((a == "búa") and (b == "kéo")) or ((a == "bao") and (b == "búa")):
        print("người chơi 1 thắng")
    else:
        print("người chơi 2 thắng")
else:
    print("giá trị nhập bị sai")