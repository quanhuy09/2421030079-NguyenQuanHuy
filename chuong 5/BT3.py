a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
min_cs = 9
tam = b
while tam > 0:
    cs = tam % 10
    if cs < min_cs:
        min_cs = cs
    tam = tam // 10
print("Chữ số nhỏ nhất của b là:",min_cs)
if min_cs != 0 and a % min_cs == 0:
    print(a,"chia hết cho",min_cs)
else:
    print(a,"không chia hết cho",min_cs)