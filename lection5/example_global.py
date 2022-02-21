

X = 88  # Глобальная переменная X


def func():
    global X
    X = 99  # Глобальная переменная X: снаружи def


func()
print(X)  # Выводит 99


y, z = 1, 2  # Глобальные переменные в модуле


def all_global():
    global x  # Объявление присваиваемой глобальной переменной
    x = y + z  # Объявлять у, z не нужно: правило LEGB (local, enclosing, global, built-in)


all_global()
print(x)
