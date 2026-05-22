m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
tong = m + n
print("Tong la:", tong)
lon_nhat = 0
while tong > 0:
    so = tong % 10
    if so > lon_nhat:
        lon_nhat = so  
    tong = tong // 10
print("Chu so lon nhat la:", lon_nhat)