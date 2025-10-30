import math
# Nhập giá trị x
x = float(input("Nhap vao so thuc x: "))

# Tính y1 và y2 theo đề
y1 = 4 * (x**2 + 10 * x * math.sqrt(x) + 3 * x + 1)
y2 = (math.sin(math.pi * x**2) + math.sqrt(x**2 + 1)) / (math.e**(2 * x) + math.cos((math.pi / 4) * x))

# In kết quả làm tròn 2 chữ số thập phân
print(f"y1 = {y1:.2f}")
print(f"y2 = {y2:.2f}")