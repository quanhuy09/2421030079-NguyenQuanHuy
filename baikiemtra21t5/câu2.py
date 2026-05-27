n = int(input("Nhập n: "))
tong = 0
while n > 0:
    tong = tong + n % 10
    n = n // 10
print("Tổng chữ số =",tong)
if tong % 3 == 0:
    print("Chia hết cho 3")
else:
    print("Không chia hết cho 3")
