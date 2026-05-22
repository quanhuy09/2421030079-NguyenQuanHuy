def nt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input("Nhap n: "))
tong = 0
for i in range(n):
    x = int(input("Nhap so: "))
    if nt(x):
        tong += x
print("Tong =", tong)
if tong % 2 != 0 and tong > 50:
    print("Dung")
else:
    print("Sai")