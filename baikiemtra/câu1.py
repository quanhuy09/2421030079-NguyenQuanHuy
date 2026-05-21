n = int(input("Nhập n: "))
tong = 0
dem = 0
for i in range(n):
    x = float(input("Nhập số: "))
    if x > 0 and x < 1000:
        tong = tong + x
        dem = dem + 1
if dem > 0:
    tbc = tong / dem
    print("Trung bình cộng =", tbc)
else:
    print("Không có số thỏa mãn")
    
