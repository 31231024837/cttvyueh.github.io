import math
# Nhập góc theo độ
degree = float(input("Nhap goc (do): "))

# Đổi sang radian
radian = degree * math.pi / 180

# In kết quả với 4 chữ số thập phân
print(f"{degree} do = {radian:.4f} radian")