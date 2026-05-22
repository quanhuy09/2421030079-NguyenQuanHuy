a = []
s = 0
n = int(input("Nhập số phần tử của dãy số:"))
for i in range(1,n+1):
    k = int(input("Nhập phần tử thứ "+str(i)+":"))
    a.append(k)
for i in a:
    s = s+i
print("Tổng số của dãy số là:"+str(s))
