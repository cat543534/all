X = float(input('вес: '))
A = float(input('цена: '))
Y = float(input('вес 2: '))
price_per_kg = A / X
cost_Y = price_per_kg * Y
print('цена за кг = ', round(price_per_kg, 2))
print(f'цена за {Y} кг = ', round(cost_Y, 2))