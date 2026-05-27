a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
tong = a + b
print ("Tổng =", tong)
max_cs = 0 
while tong > 0:
    cs = tong % 10
    if cs > max_cs:
        max_cs = cs
    tong = tong // 10
print("Chữ số lớn nhất =", max_cs)
        