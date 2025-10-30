# Nhập tổng số giây
t = int(input("Nhap vao tong so giay: "))

# Tính số giờ, phút, giây
h = t // 3600               # số giờ
m = (t % 3600) // 60        # số phút
s = t % 60                  # số giây còn lại

# In kết quả
print(f"{t} giay co dang {h}:{m}:{s}")