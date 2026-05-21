m = int(input("Nhâp m:"))
n = int(input("Nhập n:"))
tong = 0
siuu = n
while siuu > 0:
    tonng = tong + siuu % 10
    siuu = siuu // 10
print("Tổng chữ số của n =",tong)
if tong != 0:
    if m % tong == 0:
        print("m chia hết cho tổng chữ số của n")
    else:
        print("m không chia hết cho tổng chữ số của n")
else:
    print("Tổng chữ số bằng 0")
            





