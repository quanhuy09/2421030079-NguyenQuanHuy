n = int(input("Nhập n: "))
tich = 1
while n > 0:
    tich = tich *(n % 10)
    n = n // 10 
    print("Tích các chữ số =",tich)
if tich % 2 == 0 and tich > 20:
    print("Thỏa mãn")
else:
    print("Không thỏa mãn")
    