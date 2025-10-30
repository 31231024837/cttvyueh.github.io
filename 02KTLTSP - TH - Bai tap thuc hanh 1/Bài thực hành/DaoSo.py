x = int(input("Nhập số nguyên 4 chữ số x: "))

d1 = x // 1000          # hàng nghìn
d2 = (x // 100) % 10    # hàng trăm
d3 = (x // 10) % 10     # hàng chục
d4 = x % 10             # hàng đơn vị

y = d4*1000 + d3*100 + d2*10 + d1
print("Số đảo của x là:", y)