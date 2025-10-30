# Nhập điểm các môn
math = float(input("Nhập điểm Toán: "))
physic = float(input("Nhập điểm Lý: "))
chemistry = float(input("Nhập điểm Hóa: "))

# Tính điểm trung bình
dtb = (math * 2 + physic * 3 + chemistry) / 6

# Xếp loại theo DTB
if 8 <= dtb <= 10:
    rating = "Giỏi"
elif 6.5 <= dtb < 8:
    rating = "Khá"
elif 5 <= dtb < 6.5:
    rating = "Trung bình"
else:
    rating = "Yếu"

# In kết quả
print(f"Điểm trung bình = {dtb:.2f}, Xếp loại {rating}.")
