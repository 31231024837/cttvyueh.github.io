# Nhập tọa độ hai điểm
x1 = float(input("Nhap hoanh do x1: "))
y1 = float(input("Nhap tung do y1: "))
x2 = float(input("Nhap hoanh do x2: "))
y2 = float(input("Nhap tung do y2: "))

# Tính khoảng cách theo công thức: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# In kết quả với 2 chữ số thập phân
print(f"Khoang cach giua A({x1}, {y1}) va B({x2}, {y2}) la {d:.2f}")