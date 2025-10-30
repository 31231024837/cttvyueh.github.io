# Nhập số tự nhiên n (< 1000)
n = int(input("Nhập số tự nhiên n (< 1000): "))

if n < 0 or n >= 1000:
    print("Số không hợp lệ!")
else:
    # a) Đếm số chữ số
    num_digits = len(str(n))

    # b) Tính tổng các chữ số
    sum_digits = sum(int(d) for d in str(n))

    # c) Chữ số cuối
    last_digit = n % 10

    # d) Chữ số đầu
    first_digit = int(str(n)[0])

    # In kết quả
    print(f"{n} has {num_digits} digits.")
    print(" + ".join(str(d) for d in str(n)), "=", sum_digits)
    print(f"Last digit is {last_digit}.")
    print(f"First digit is {first_digit}.")
