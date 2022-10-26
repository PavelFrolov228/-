n = int(input("Введите количество элементов списка: "))
n_min = int(input("Введите минимальный порог: "))
n_max = int(input("Введите максимальный порог: "))
kol = 0

from random import uniform

lst_random = [uniform(-10, 10) for i in range(n)]
print(lst_random)
print("Количество подходящих чисел: ", kol)

/я тебя люблю