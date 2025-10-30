# Nhập số tự nhiên có 4 chữ số
n = int(input("Nhập số tự nhiên có 4 chữ số: "))

# Kiểm tra tính hợp lệ
if n < 1000 or n > 9999:
    print("Số không hợp lệ! Vui lòng nhập số có 4 chữ số.")
else:
    # Cách 1: Dùng chia lấy dư
    a = n // 1000          # chữ số hàng nghìn
    b = (n // 100) % 10    # chữ số hàng trăm
    c = (n // 10) % 10     # chữ số hàng chục
    d = n % 10             # chữ số hàng đơn vị

    vmax = max(a, b, c, d)

    # In kết quả
    print(f"Chữ số lớn nhất của {n} là {vmax}")