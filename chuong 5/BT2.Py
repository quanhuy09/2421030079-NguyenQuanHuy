n = int(input("Nhap sp phan tu n:"))
a = []
for i in range(n):
    x = int(input(f"Nhap phan tu thu {i+1}:"))
    a.append(x)
tong = 0
for x in a:
    if x % 2  == 0:
        tong +=x
print("Tong cac phan tu chan =",tong)
if tong % 7 == 0 and tong < 200:
    print("Tong chia het cho 7 va nho hon 200")
else:
    print("Tong khong thoa man dieu kien")