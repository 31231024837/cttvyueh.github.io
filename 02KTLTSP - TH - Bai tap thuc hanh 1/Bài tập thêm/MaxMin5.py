# Nhập 5 số nguyên
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
d = int(input("Nhập d: "))
e = int(input("Nhập e: "))

# Tính giá trị lớn nhất và nhỏ nhất
vmax = max(a, b, c, d, e)
vmin = min(a, b, c, d, e)

# In kết quả
print("Giá trị nhỏ nhất là", vmin)
print("Giá trị lớn nhất là", vmax)