n = int(input("Nhap so phan tu n = "))
tong = 0
dem = 0
for i in range(n):
    x = float(input("Nhap x[%d] = " % i))
    if -1000 < x < -10:
        tong = tong + x
        dem = dem + 1
if dem > 0:
    tbc = tong / dem
    print("Trung binh cong =", tbc)
else:
    print("Khong co phan tu thoa man")