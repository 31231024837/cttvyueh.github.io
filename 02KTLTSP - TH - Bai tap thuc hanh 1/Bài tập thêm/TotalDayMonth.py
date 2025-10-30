# Nhập tháng và năm
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Kiểm tra tính hợp lệ
if month < 1 or month > 12:
    print("Tháng không hợp lệ!")
else:
    # Xác định số ngày
    if month in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    elif month in (4, 6, 9, 11):
        days = 30
    elif month == 2:
        # Kiểm tra năm nhuận
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days = 29
        else:
            days = 28
    # Xuất kết quả
    print("Tháng %d năm %d có %d ngày." % (month, year, days))