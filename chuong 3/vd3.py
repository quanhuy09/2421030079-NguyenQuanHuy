def giaithua(m):
    gt = 1 
    for i in range(1,m+1):
        gt = gt*i
    return gt 
n = int(input("Nhập vào một số nguyên dương: "))
print("%d! = %d" %(n,giaithua(n)))
