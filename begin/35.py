V = float(input('скорость лодки в стоячей воде: '))
U = float(input('скорость течения реки: '))
T1 = float(input('время движения лодки по озеру: '))
T2 = float(input('время движения лодки по реке: '))
if V < U:
    print("неправильно")
else:
    S = V * T1 + V * T2
    print(round(S, 2))