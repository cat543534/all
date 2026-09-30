A = float(input("число: "))
B = float(input("число: "))
C = float(input("число: "))
if C > A and C < B:
    AC = (abs(C - A))
    BC = (abs(C - B))
    print(round(AC, 2))
    print(round(BC, 2))
else:
    print("неправильно")