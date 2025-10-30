# Nhập vào giờ, phút, giây
h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))
s = int(input("Nhap so giay: "))

# Tính tổng số giây
tong_giay = h * 3600 + m * 60 + s

# In kết quả
print(f"Tong so giay cua {h}:{m}:{s} la {tong_giay} giay")