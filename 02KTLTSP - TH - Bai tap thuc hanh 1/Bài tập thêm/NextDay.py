# Nhập ngày, tháng, năm
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Xác định số ngày trong tháng
def days_in_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        # năm nhuận
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28

# Tính ngày kế tiếp
day += 1
if day > days_in_month(month, year):
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1

# In kết quả
print("Ngày kế tiếp là: %02d/%02d/%04d" % (day, month, year))
