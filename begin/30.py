p = 3.14
a = float(input("число: "))
if a <= 0 or a >= 2*p:
    print("неправильно a должно быть [0, 2*pi]")
else:
    R = p * a / 180
    print(f"R = {R}")