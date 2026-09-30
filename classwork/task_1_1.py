import sys
print('Версия Python:', sys.version.split()[0])
print('Интерпретатор:', sys.executable)
print('Количество путей поиска:', len(sys.path))
for i in sys.path[:4]:
    print('', i)
import math, random
print('math.pi =', math.pi)
print('random.random() =',random.random())
print('Загруженно модулей:', len(sys.modules))
print('Пример:', sorted(sys.modules)[:5])
public = [n for n in dir(math) if not n.startswith('_')]
print('Публичных имён в math:', len(public))
print('Первые 8:', public[:8])
print('Мой __name__ =', __name__)