# Nhập hệ số a, b, c
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Trường hợp a = 0 (phương trình bậc nhất hoặc vô số nghiệm)
if a == 0:
    if b == 0:
        if c == 0:
            print("Unlimited solutions")
        else:
            print("No solution")
    else:
        x = -c / b
        print("x=%.2f" % x)
else:
    # Tính delta
    delta = b**2 - 4*a*c
    if delta < 0:
        print("No solution")
    elif delta == 0:
        x = -b / (2*a)
        print("x1=%.2f" % x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("x1=%.2f, x2=%.2f" % (x1, x2))