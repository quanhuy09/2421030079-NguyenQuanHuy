with open("input.txt","r",ecoding="utf-8")as f:
    data = f.read()
    so=""
    chu=""
for c in data:
    if c.isdigit():
        so += c
    elif c.isalpha() or c.isspace():
        chu += c
with open("outso.txt", "w",ecoding="utf-8") as f:
    f.write(so)
with open("outchu.txt", "w",ecoding="utf-8") as f:
    f.write(chu)
print("Đã xong!")
